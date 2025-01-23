from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse


class AdminSiteTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            username="test_admin",
            password="test_password",
        )
        self.client.force_login(self.admin_user)
        self.redactor = get_user_model().objects.create_user(
            username="test_redactor",
            password="test_password",
            years_of_expirience=5,
        )

    def test_redactor_years_of_expirience_listed(self):
        url = reverse("admin:accounts_redactor_changelist")
        res = self.client.get(url)
        self.assertContains(res, self.redactor.years_of_expirience)
