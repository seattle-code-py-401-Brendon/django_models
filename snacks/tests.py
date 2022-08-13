from django.test import TestCase
from django.urls import reverse


# Create your tests here.
class Snacks_project_test(TestCase):

    def test_home_page_status_code(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_home_page_templates(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'snack_list.html')
