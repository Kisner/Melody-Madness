from django.test import SimpleTestCase
from django.urls import reverse, resolve
from welcome.views import index

class TestUrls(SimpleTestCase):
    def test_welcome_url_is_resolved(self):
        url = reverse('auth')
        print(resolve(url))
        self.assertEquals(resolve(url).func, '')