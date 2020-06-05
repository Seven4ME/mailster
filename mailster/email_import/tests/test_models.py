from django.test import TestCase
from django.urls import reverse, resolve

from ..models import Contact, Campaign
from django.contrib.auth.models import User

class ContactCreationTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.campaign = Campaign.objects.create(campaign_name='testing_campaign', user=self.user)
        Contact.objects.create(email='test@gmail.com', is_valid=False, campaign_name=self.campaign)

    def test_contact_is_existing_email(self):
        test_email = Contact.objects.get(email='test@gmail.com')
        self.assertEquals(test_email.email, 'test@gmail.com')
