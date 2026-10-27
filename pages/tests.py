from django.test import TestCase
from django.urls import reverse

class PageTests(TestCase):
    def test_home(self):
        r = self.client.get(reverse("home"))
        self.assertEqual(r.status_code, 200)
        self.assertContains(r, "Welcome!")

    def test_extra(self):
        self.assertEqual(self.client.get(reverse("extra")).status_code, 200)

    def test_phantasm(self):
        self.assertEqual(self.client.get(reverse("phantasm")).status_code, 200)