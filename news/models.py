from django.db import models
from django.conf import settings


class Topic(models.Model):
    name = models.CharField(max_length=255)
    class Meta:
        ordering = ["name"]
        
    def __str__(self):
        return self.name
    
    
class Newspaper(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    published_date = models.DateField()
    topics = models.ManyToManyField(
        Topic,
        related_name="newspapers"
    )
    publishers = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="newspapers"
    )
    
    def __str__(self):
        return f"{self.title}: {self.content}"
