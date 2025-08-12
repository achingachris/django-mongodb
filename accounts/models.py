from django.conf import settings
from django.db import models
from django_mongodb_backend.fields import ObjectIdAutoField


class FavoriteTalk(models.Model):
    id = ObjectIdAutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="favorite_talks")
    title = models.CharField(max_length=255)
    speaker = models.CharField(max_length=255)
    notes = models.TextField(blank=True)
    presentation_link = models.URLField()
    user_notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.title} by {self.speaker}"
