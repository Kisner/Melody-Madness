from django.test import SimpleTestCase
from django.urls import reverse, resolve
from generate.views import index

class TestUrls(SimpleTestCase):

    def test_generate_url_is_resolved(self):
        """
        Gets the generate screen url that is called and compares it to the actual to check
        :return: None
        """
        print("check")
        url = reverse('index')
        self.assertEquals(resolve(url).func, index)

