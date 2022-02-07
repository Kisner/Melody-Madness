from django.test import TestCase, Client
from django.urls import reverse
import json

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.welcome_url = reverse('welcome')

    def test_project_welcome_GET(self):
        response = self.client.get(self.welcome_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'welcome/welcome.html')
