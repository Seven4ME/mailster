from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
import uuid

# Create your models here.
class Campaign(models.Model):
    campaign_name = models.CharField(max_length=255, default="")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.campaign_name


class Contact(models.Model):
    email = models.EmailField()
    created_at = models.DateField(auto_now_add=True)
    is_valid = models.BooleanField()
    campaign_name = models.ForeignKey(Campaign, on_delete=models.CASCADE)

    def __str__(self):
        return self.email

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
    email_text = RichTextField(blank=True, null=True)
    email_subject = models.CharField(max_length=255, default="")

    def __str__(self):
        return self.template_name

class Sending(models.Model):
    """Журнал отправленных сообщений пользователям."""

    STATUS = (
        ('new', 'new'),
        ('pending', 'pending'),
        ('done', 'done'),
    )
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    campaign_name = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    template_name = models.ForeignKey(Template, on_delete=models.CASCADE)
    email = models.ForeignKey(Contact, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=STATUS, default='new')
    is_opened = models.BooleanField(default=False)




