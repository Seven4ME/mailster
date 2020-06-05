from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from django.template import Context, Template
from django.views.generic import ListView, CreateView, UpdateView, DetailView
# Create your views here.
from decouple import config
import uuid
from rest_framework import generics
from rest_framework.response import Response
from .seriallizers import EmailOpenSerializer

from .models import Campaign, Contact, Sending
from .models import Template as TemplateModel
from django.contrib.auth.decorators import login_required

from .tasks import send_email_task
from django.shortcuts import get_object_or_404


#For test made test smtp server, using: python -m smtpd -n -c DebuggingServer localhost:1025
def sending_email_example(request, **kwargs):
    # получаем шаблон
    template_id = request.GET['template_id']
    tmpl = TemplateModel.objects.get(id=template_id)
    recepients = Contact.objects.filter(campaign_name=tmpl.campaigns).all().values('id', 'email')

    for emails in recepients:
        generated_uuid = uuid.uuid4()
        context = Context({
            'email': emails,
            'user_uuid': generated_uuid,
        })
        # рендерим шаблон
        template = Template(tmpl.email_text)
        rendered_email = template.render(context)
        from_email = config('EMAIL_HOST')
        api_url = config('API_EMAIL_ROUTE')
        api_key = config('API_EMAIL_SECRET_KEY')
        to_email = [emails['email']]
        save_to_db = Sending(uuid=generated_uuid, campaign_name_id=tmpl.campaigns.id, email_id=emails['id'],
                                 template_name_id=template_id)
        save_to_db.save()
        send_email_task(api_url,api_key,tmpl.email_subject, rendered_email, to_email, from_email)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


@login_required
def dashboard(request):
    return render(request, 'base_dashboard.html', {})

class CampaignList(ListView):
    paginate_by = 5
    model = Campaign

class CampaignCreate(CreateView):
    model = Campaign
    fields = ['campaign_name', 'user']
    success_url = '/email_import/dashboard/campaigns'

    def get_form_kwargs(self):
        """Перехватываем kwargs, который передаётся в форму и добавляем нужные нам данные"""
        kwargs = super().get_form_kwargs()
        # так как kwargs['data'] изначатьно иммутабельный QueryDict мы его делаем мутабельным через copy()
        if data := kwargs.get('data'):
            modified_data = data.copy()
            # добавляем нужный нам ключ и значение в словарь,
            # надо обратить внимание что это работает только для авторизованной сессии
            modified_data['user'] = self.request.user.id
            # заменяем kwargs['data'] на измененный словарь
            kwargs['data'] = modified_data
        return kwargs

class CampaignUpdate(UpdateView):
    model = Campaign
    fields = ['campaign_name']
    success_url = '/email_import/dashboard/campaigns'


class CampaignInfo(DetailView):
    model = Campaign
    def get_context_data(self, **kwargs):
        context = super(CampaignInfo, self).get_context_data(**kwargs)
        context['related_campaigns'] = TemplateModel.objects.filter(campaigns_id=self.kwargs['pk'])
        return context


def campaign_post(request):
    if request.method == 'POST':
        post_data = request.POST
        save_to_db = Sending(campaign_name_id=post_data['campaign_name'], email_id=post_data['email'],
                             template_name_id=post_data['template_name'])
        save_to_db.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

class PixelView(generics.CreateAPIView):
    serializer_class = EmailOpenSerializer
    lookup_url_kwarg = "uuid"

    def get(self, request, **kwargs):
        uuid = self.kwargs.get(self.lookup_url_kwarg)
        sending_obj = get_object_or_404(Sending, uuid=uuid)
        sending_obj.is_opened = True
        sending_obj.save()
        is_existing_uuid = 'Status of UUID: {} was changed'.format(uuid)
        return Response(is_existing_uuid)


class TemplateCreate(CreateView):
    model = TemplateModel
    fields = ['campaigns', 'template_name', 'email_text', 'email_subject']
    success_url = '/email_import/dashboard/campaigns'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if data := kwargs.get('data'):
            modified_data = data.copy()
            modified_data['campaigns'] = self.kwargs['pk']
            kwargs['data'] = modified_data
        return kwargs

class TemplateUpdate(UpdateView):
    model = TemplateModel
    fields = ['template_name', 'email_text']
    success_url = '/email_import/dashboard/campaigns'

class ContactList(ListView):
    paginate_by = 5
    model = Contact

class ContactCreate(CreateView):
    model = Contact
    fields = ['email', 'is_valid', 'campaign_name']
    success_url = '/email_import/dashboard/contacts'

class ContactUpdate(UpdateView):
    model = Contact
    fields = ['email', 'is_valid', 'campaign_name']
    success_url = '/email_import/dashboard/contacts'

