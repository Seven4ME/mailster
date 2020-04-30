from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Contact, Campaign

# Register your models here.
@admin.register(Contact)
class ContactAdmin(ImportExportModelAdmin):
    pass

@admin.register(Campaign)
class CampaignAdmin(ImportExportModelAdmin):
    pass
