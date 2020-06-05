from django.test import TransactionTestCase
from django.urls import reverse, resolve
from ..views import dashboard, CampaignList, CampaignCreate, CampaignUpdate, CampaignInfo, TemplateCreate, TemplateUpdate

from django.test import Client
from django.contrib.auth.models import User



class TestUrls(TransactionTestCase):
    def test_login_status(self):
        user = User.objects.create(username='testuser')
        user.set_password('12345')
        user.save()
        c = Client()
        logged_in = c.login(username='testuser', password='12345')
        self.assertEquals(logged_in, True)

    def test_dashboard_url_is_resolved(self):
        url = reverse('dashboard')
        self.assertEquals(resolve(url).func, dashboard)

    def test_url_dashboard_status(self):
        user = User.objects.create(username='testuser')
        user.set_password('12345')
        user.save()
        c = Client()
        logged_in = c.login(username='testuser', password='12345')
        response = c.get(reverse('dashboard'))
        self.assertEquals(response.status_code,200)




    def test_campaign_list_url_is_resolved(self):
        url = reverse('campaigns_list')
        self.assertEquals(resolve(url).func.__name__, CampaignList.as_view().__name__)

    def test_campaign_list_url_status(self):
        response = self.client.get(reverse('campaigns_list'))
        self.assertEqual(response.status_code, 302)

    def test_campaign_create_url_is_resolved(self):
        url = reverse('campaigns_create')
        self.assertEquals(resolve(url).func.__name__, CampaignCreate.as_view().__name__)

    def test_campaign_create_url_status(self):
        response = self.client.get(reverse('campaigns_create'))
        self.assertEquals(response.status_code, 302)

    def test_campaign_update_url_is_resolved(self):
        url = reverse('campaigns_update', args=[1])
        self.assertEquals(resolve(url).func.__name__, CampaignUpdate.as_view().__name__)

    def test_campaign_update_url_status(self):
        response = self.client.post(reverse('campaigns_update', args=(1, )))
        self.assertEquals(response.status_code, 302)

    def test_campaign_info_url_is_resolved(self):
        url = reverse('companies_info', args=[1])
        self.assertEquals(resolve(url).func.__name__, CampaignInfo.as_view().__name__)

    def test_campaign_info_url_status(self):
        response = self.client.post(reverse('companies_info', args=(1, )))
        self.assertEquals(response.status_code, 302)

    def test_template_create_url_is_resolved(self):
        url = reverse('create_template', args=[1])
        self.assertEquals(resolve(url).func.__name__, TemplateCreate.as_view().__name__)

    def test_template_create_url_status(self):
        response = self.client.post(reverse('create_template', args=(1,)))
        self.assertEquals(response.status_code, 302)

    def test_template_update_url_is_resolved(self):
        url = reverse('update_template', args=[1])
        self.assertEquals(resolve(url).func.__name__, TemplateUpdate.as_view().__name__)

    def test_template_update_url_status(self):
        response = self.client.post(reverse('update_template', args=(1,)))
        self.assertEquals(response.status_code, 302)
