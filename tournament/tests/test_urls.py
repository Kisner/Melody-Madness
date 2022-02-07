from django.test import SimpleTestCase
from django.urls import reverse, resolve
from tournament.views import index


class TestUrls(SimpleTestCase):

    def test_tournament_url_is_resolved(self):
        """
        Gets the generate screen url that is called and compares it to the actual to check
        :return: None
        """
        url = reverse('tournament')
        self.assertEquals(resolve(url).func, index)
