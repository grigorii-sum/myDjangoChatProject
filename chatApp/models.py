from django.db import models
from django.conf import settings
from django.utils import timezone


class Message(models.Model):
    author_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text

    @classmethod
    def create(cls, author_id, text):
        message = cls(author_id=author_id, text=text)
        return message
