from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Contact, Campaign, Sending, Template

# Register your models here.
@admin.register(Contact)
class ContactAdmin(ImportExportModelAdmin):
    pass

class SendingInlineCampaign(admin.TabularInline):
    model = Sending

@admin.register(Campaign)
class CampaignAdmin(ImportExportModelAdmin):
    inlines = [
        SendingInlineCampaign
    ]
