from django.db import models

# Create your models here.
class Contacts(models.Model):
    email = models.EmailField(),
    created_at = models.DateField(),
    isValid = models.BooleanField(),
    campaign_name = models.CharField(max_length=255)

class Last_sending(models.Model):
    contacts = models.ForeignKey(Contacts, on_delete=models.CASCADE)
    email = models.EmailField(),
    last_email = models.DateField()

class Campaigns(models.Model):
    campaign_name = models.CharField(max_length=255),
    user_id = models.IntegerField(),
    template_name = models.CharField(max_length=255)

class Statistic(models.Model):
    campaigns = models.ForeignKey(Campaigns, on_delete=models.CASCADE),
    campaign_name = models.CharField(max_length=255),
    isOpened = models.BooleanField(),
    emails_count = models.IntegerField(),
    date = models.DateField()

class Templates(models.Model):
    campaigns = models.ForeignKey(Campaigns, on_delete=models.CASCADE),
    template_name = models.CharField(max_length=255)





