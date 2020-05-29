from celery import shared_task
from django.core.mail import send_mail
import requests

@shared_task
def send_email_task(api_url,api_key, subject, rendered_email, contacts_list, email_hoster):
    #task for api
    response = requests.post(
        api_url,
        auth=('api', api_key),
        data = {
            'from': 'test <mailgun@{}>'.format(email_hoster),
            'to': contacts_list,
            'subject': subject,
            'html': rendered_email
        }
    )
    json_response = response.json()
    if response.status_code == 200 and json_response['message'] == 'Queued. Thank you.':
        print('Sended')
    else:
        print('Cant send, coz:{}'.format(json_response['message']))
    #task for smtp
    #send_mail(
    #    subject,
    #    str(rendered_email),
    #    email_hoster,
    #    contacts_list,
    #    fail_silently=False,
    #)
    return None

