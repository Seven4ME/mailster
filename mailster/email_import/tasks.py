from celery import shared_task
from django.core.mail import send_mail
from decouple import config
from time import sleep
from .models import Contact

@shared_task
def send_email_task(tmpl, rendered_email, contacts_list):
    sleep(10)
    send_mail(
        tmpl.email_subject,
        str(rendered_email),
        config('EMAIL_HOST_USER'),
        contacts_list,
        fail_silently=False,
    )
    return None

