from django.test import TestCase
from userprofile.models import models

class MyModelTestCase(TestCase):
    def test_something_about_my_model(self):
        obj = models()
        self.assertEqual(obj.my_method(), 'Expected result')
