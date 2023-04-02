import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_project.settings")

import django
django.setup()


from django.db import models

class Article(models.Model):

    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title

class Comment(models.Model):
    author = models.CharField(max_length=128)
    message = models.CharField(max_length=255)
    # relacja wiele do jednego (wiele komenatrzy może wskazywać jeden artykuł)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    def __str__(self):
        return self.author + ":" + self.message




