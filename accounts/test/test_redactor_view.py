from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse

from accounts.models import Redactor

User = get_user_model()


class RedactorViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.redactor = Redactor.objects.create_user(
            username="testuser",
            password="testpassword",
            email="testuser@example.com",
            years_of_expirience=5,
        )

    def test_redactor_list_view(self):
        response = self.client.get(reverse("accounts:redactor-list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "accounts/redactor_list.html")
        self.assertIn(self.redactor, response.context["redactor_list"])

    def test_redactor_register_view_get(self):
        response = self.client.get(reverse("accounts:sign-up"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/register.html")

    def test_redactor_register_view_post(self):
        data = {
            "username": "newuser",
            "password1": "securepassword123",
            "password2": "securepassword123",
            "email": "newuser@example.com",
        }
        response = self.client.post(reverse("accounts:sign-up"), data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("news:index"))
        self.assertTrue(Redactor.objects.filter(username="newuser").exists())

    def test_redactor_update_view_get(self):
        self.client.login(username="testuser", password="testpassword")
        response = self.client.get(
            reverse(
                "accounts:redactor-update", kwargs={"pk": self.redactor.pk}
            )
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "accounts/redactor_form.html")
        self.assertEqual(response.context["object"], self.redactor)

    def test_redactor_update_view_post(self):
        self.client.login(username="testuser", password="testpassword")
        data = {
            "email": "updatedemail@example.com",
            "first_name": "updated",
            "last_name": "name",
            "years_of_expirience": 10,
        }
        response = self.client.post(
            reverse(
                "accounts:redactor-update", kwargs={"pk": self.redactor.pk}
            ),
            data,
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("accounts:redactor-list"))
        self.redactor.refresh_from_db()
        self.assertEqual(self.redactor.email, "updatedemail@example.com")
        self.assertEqual(self.redactor.first_name, "updated")
        self.assertEqual(self.redactor.last_name, "name")
        self.assertEqual(self.redactor.years_of_expirience, 10)
