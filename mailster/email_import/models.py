from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Campaign(models.Model):
    campaign_name = models.CharField(max_length=255),
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

class Contacts(models.Model):
    email = models.EmailField(),
    created_at = models.DateField(auto_now_add=True),
    is_valid = models.BooleanField(),
    campaign_name = models.ForeignKey(Campaign, on_delete=models.CASCADE)

class LastSending(models.Model):
    contacts = models.ForeignKey(Contacts, on_delete=models.CASCADE)
    email = models.EmailField(),
    last_email = models.DateField()


class Statistic(models.Model):
    campaign_name = models.CharField(max_length=255),
    isOpened = models.BooleanField(),
    emails_count = models.IntegerField(),
    date = models.DateField()

class Templates(models.Model):
    campaigns = models.ForeignKey(Campaign, on_delete=models.CASCADE),
    template_name = models.CharField(max_length=255),
    email_text = models.TextField(default="")





