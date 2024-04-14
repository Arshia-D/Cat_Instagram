from django.test import TestCase
from django.urls import reverse

class SecurityTest(TestCase):
    def test_no_sql_injection(self):
        response = self.client.get(reverse('my-view'), {'param': '1 OR 1=1'})
        self.assertNotEqual(response.status_code, 200, "SQL Injection attempt detected!")