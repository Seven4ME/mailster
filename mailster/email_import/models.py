from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Campaign(models.Model):
    campaign_name = models.CharField(max_length=255, default="")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Contact(models.Model):
    email = models.EmailField()
    created_at = models.DateField(auto_now_add=True)
    is_valid = models.BooleanField()
    campaign_name = models.ForeignKey(Campaign, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('contact-detail', kwargs={'pk': self.pk})


class LastSending(models.Model):
    contacts = models.ForeignKey(Contact, on_delete=models.CASCADE)
    email = models.EmailField(default="")
    last_email = models.DateField()


class Statistic(models.Model):
    campaigns = models.ForeignKey(Campaign, on_delete=models.CASCADE, null=True)
    is_opened = models.BooleanField(default=False)
    emails_count = models.IntegerField(default=0)
    date = models.DateField()

class Template(models.Model):
    campaigns = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    template_name = models.CharField(max_length=255)
    email_text = models.TextField(default="")





