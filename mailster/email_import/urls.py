from django.urls import path, include
from .views import CampaignList, dashboard, CampaignCreate, ContactList, ContactCreate, ContactUpdate

urlpatterns = [
    path('dashboard/', dashboard, name="dashboard"),
    path('dashboard/campaigns',CampaignList.as_view(template_name="companies.html"), name="campaigns_list"),
    path('dashboard/campaigns/create', CampaignCreate.as_view(template_name="companies_create.html")),
    path('dashboard/contacts', ContactList.as_view(template_name="contacts.html"), name="contacts_list"),
    path('dashboard/contacts/create', ContactCreate.as_view(template_name="contacts_create.html"), name="contacts_create"),
    path('dashboard/contacts/update/<int:pk>/', ContactUpdate.as_view(template_name="contacts_update.html"), name="contacts_update"),
]