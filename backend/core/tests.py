from django.test import TestCase
from django.urls import reverse
class HealthTest(TestCase):
 def test_health(self):
  r=self.client.get('/api/health/'); self.assertEqual(r.status_code,200); self.assertEqual(r.json()['status'],'ok')
