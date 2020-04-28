from django.contrib import admin
from import_export import resources
from .models import Contact

# Register your models here.
class ContactResource(resources.ModelResource):
    class Meta:
        model = Contact
        fields = ('email', 'created_at', 'is_valid', 'campaign_name')

