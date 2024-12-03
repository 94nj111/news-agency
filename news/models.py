from django.db import models
from django.conf import settings
from django.urls import reverse
from django_resized import ResizedImageField


class Topic(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("news:topic-detail", kwargs={"pk": self.pk})


class Newspaper(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    published_date = models.DateField(auto_now_add=True)
    topics = models.ManyToManyField(Topic, related_name="newspapers")
    publishers = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="newspapers"
    )
    photo = ResizedImageField(
        upload_to="images/",
        null=True,
        blank=True,
        force_format="WEBP",
        quality=75,
    )

    class Meta:
        ordering = ["-published_date"]

    def __str__(self):
        return f"{self.title}: {self.content}"

    def get_absolute_url(self):
        return reverse("news:newspaper-detail", kwargs={"pk": self.pk})
