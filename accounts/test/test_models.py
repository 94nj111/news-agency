from django.contrib.auth import get_user_model
from django.test import TestCase


class ModelTest(TestCase):
    def test_redactor_create_with_years_of_expirience(self):
        username = "test_username"
        password = "test_password"
        years_of_expirience = 5
        redactor = get_user_model().objects.create_user(
            username=username,
            password=password,
            years_of_expirience=years_of_expirience,
        )
        self.assertEqual(redactor.username, username)
        self.assertTrue(redactor.check_password(password))
        self.assertEqual(redactor.years_of_expirience, years_of_expirience)
