from django.test import TestCase
from django.urls import reverse
from userprofile.models import models

class ViewIntegrationTest(TestCase):
    def test_model_creation_through_view(self):
        # Send a POST request to the view with the given data
        response = self.client.post(reverse('my-view'), data={'field': 'value'})

        # Assert that the response has a status code of 200
        self.assertEqual(response.status_code, 200)

        # Assert that an instance of models has been created
        self.assertTrue(models.objects.exists())