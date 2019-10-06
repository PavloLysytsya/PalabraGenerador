from django.conf import settings
from django.db import models
from django.utils import timezone


class Vocabulary(models.Model):
    word = models.TextField()
    spanish_word = models.TextField()
    native_language = models.CharField(max_length=2)
    created_at = models.DateTimeField(default=timezone.now)

    def add(self):
        self.created_at = timezone.now()
        self.save()

    def __str__(self):
        return self.word
