from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=512)
    content = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
