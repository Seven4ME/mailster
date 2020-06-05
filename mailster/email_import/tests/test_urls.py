from django.test import SimpleTestCase
from django.urls import reverse, resolve
from ..views import dashboard

class TestUrls(SimpleTestCase):
    def test_dashboard_url_is_resolved(self):
        url = reverse('dashboard')
        self.assertEquals(resolve(url).func, dashboard)