from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
# Create your views here.

from django.shortcuts import HttpResponse

from .tasks import celery_task

from .models import Campaign, Contact

def celery_view(request):
    for counter in range(2):
        celery_task.delay(counter)
    return HttpResponse("FINISH PAGE LOAD")

def dashboard(request):
    return render(request, 'base_dashboard.html', {})

class CampaignList(ListView):
    paginate_by = 5
    model = Campaign

class CampaignCreate(CreateView):
    model = Campaign
    fields = ['campaign_name', 'user']
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