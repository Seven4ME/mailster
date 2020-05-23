from celery import shared_task
from django.core.mail import send_mail
from decouple import config
from time import sleep
from .models import Contact

@shared_task
def send_email_task(subject, rendered_email, contacts_list, email_hoster):
    send_mail(
        subject,
        str(rendered_email),
        email_hoster,
        contacts_list,
        fail_silently=False,
    )
    return None

