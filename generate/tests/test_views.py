from django.test import TestCase, Client
from django.urls import reverse

class TestViews(TestCase):

    def setUp(self):
        """
        Sets up the variables for different tests of the views
        :return: None
        """
        self.client = Client()
        self.gen_url = reverse('index')

    def test_project_list_GET(self):
        """
        Checks the response status code to ensure we were able to access the view
        Checks that the template used is the one specified in the html
        :return: None
        """
        response = self.client.get(self.gen_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'generate/index.html')
