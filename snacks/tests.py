from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Snack

# Create your tests here.
# Creates database, then breaks it down at the end

class SnackTests(TestCase):
# setup MUST be named exactly
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='tester',
            email='tester@email.com',
            password='password'
        )
        self.snack = Snack.objects.create(
            name='test_snack',
            description='test description',
            purchaser=self.user
        )

    def test_string_representation(self):
       self.assertEqual(str(self.snack), 'test_snack')

    def test_snack_name(self):
       self.assertEqual(f'{self.snack.name}', 'test_snack')

    def test_list_page_status_code(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_list_snack_template(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'snack_list.html')
        self.assertTemplateUsed(response, '_base.html')