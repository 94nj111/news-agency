from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django_resized import ResizedImageField


class Redactor(AbstractUser):
    has_access = models.BooleanField(default=False)
    years_of_expirience = models.PositiveIntegerField(blank=True, null=True)
    photo = ResizedImageField(
        upload_to="images/",
        null=True,
        blank=True,
        force_format="WEBP",
        quality=75,
    )

    def get_absolute_url(self):
        return reverse("accounts:redactor-detail", kwargs={"pk": self.pk})
