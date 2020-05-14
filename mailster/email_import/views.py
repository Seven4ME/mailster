from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DetailView

from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.


from .models import Campaign, Contact, Template, Sending
from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory


def sending_email_example(request, **kwargs):
    campaign_id = Sending.objects.filter(campaign_name_id=kwargs['pk']).get()
    letter_content = Template.objects.filter(id=campaign_id.template_name_id).get()
    response = HttpResponse(content=letter_content)
    response['Content-Disposition'] = 'attachment; filename="email_example.html"'
    return response



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
        context['related_campaigns'] = Template.objects.filter(campaigns_id=self.kwargs['pk'])
        SendingFormSet = inlineformset_factory(Contact, Sending, fields=('email', 'template_name', 'campaign_name'),extra=1)
        context['inline_form'] = SendingFormSet
        context['is_existing'] = Sending.objects.filter(campaign_name_id=self.kwargs['pk']).exists()
        context['pk'] = self.kwargs['pk']
        return context
def campaign_post(request):
    if request.method == 'POST':
        post_data = request.POST
        save_to_db = Sending(campaign_name_id=post_data['campaign_name'], email_id=post_data['email'],
                             template_name_id=post_data['template_name'])
        save_to_db.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


class TemplateCreate(CreateView):
    model = Template
    fields = ['campaigns', 'template_name', 'email_text']
    success_url = '/email_import/dashboard/campaigns'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if data := kwargs.get('data'):
            modified_data = data.copy()
            modified_data['campaigns'] = self.kwargs['pk']
            kwargs['data'] = modified_data
        return kwargs

class TemplateUpdate(UpdateView):
    model = Template
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