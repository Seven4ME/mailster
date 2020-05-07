from django.urls import path, include
from .views import CampaignList, dashboard, CampaignCreate, ContactList, ContactCreate, ContactUpdate, CampaignUpdate
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('dashboard/', dashboard, name="dashboard"),
    path('dashboard/campaigns',login_required(CampaignList.as_view(template_name="companies.html")), name="campaigns_list"),
    path('dashboard/campaigns/create', login_required(CampaignCreate.as_view(template_name="companies_create.html"))),
    path('dashboard/campaigns/update/<int:pk>/', login_required(CampaignUpdate.as_view(template_name="companies_update.html")), name="campaigns_update"),
    path('dashboard/contacts', login_required(ContactList.as_view(template_name="contacts.html")), name="contacts_list"),
    path('dashboard/contacts/create', login_required(ContactCreate.as_view(template_name="contacts_create.html")), name="contacts_create"),
    path('dashboard/contacts/update/<int:pk>/', login_required(ContactUpdate.as_view(template_name="contacts_update.html")), name="contacts_update"),
]