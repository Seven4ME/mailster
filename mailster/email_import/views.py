from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import Context, Template
from django.views.generic import ListView, CreateView, UpdateView, DetailView
# Create your views here.
from decouple import config


from .models import Campaign, Contact, Sending
from .models import Template as TemplateModel
from django.contrib.auth.decorators import login_required

from django.core.mail import send_mail
from django.contrib import messages
from .tasks import send_email_task

#For test made test smtp server, using: python -m smtpd -n -c DebuggingServer localhost:1025
def sending_email_example(request, **kwargs):
    # получаем шаблон
    template_id = request.GET['template_id']
    tmpl = TemplateModel.objects.get(id=template_id)
    recepients = Contact.objects.filter(campaign_name=tmpl.campaigns).all().values('email')

    contacts_list = list()

    for emails in recepients:
        contacts_list.append(emails['email'])
        context = Context({
            'email': emails
        })
        # рендерим шаблон
        template = Template(tmpl.email_text)
        rendered_email = template.render(context)

        send_email_task(tmpl, rendered_email, contacts_list)

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


class TemplateCreate(CreateView):
    model = TemplateModel
    fields = ['campaigns', 'template_name', 'email_text', 'email_subject', 'email_sender']
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