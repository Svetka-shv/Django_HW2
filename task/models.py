from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.title