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

# 1 do wielu
# 1 artykułu
# wiele komentarzy
# gdzie postawić Foreign Key ? artyułu / komentarzy ?
# komentarz1(FK) -> artykuł
# komentarz2(FK) -> artykuł

# class Article(models.Model):   #dziedzicze z modelu Django
#     title = models.CharField(max_length=255)  #pole tekstowe
#     author = models.CharField(max_length=128)
#     description = models.TextField() #textfild nieograniczona ilosc znakow
#
# #metoda zwracajaca tytył atykułu
#     def __str__(self):
#         return self.title
#
#
# class Comment(models.Model):
#     author = models.CharField(max_length=128)
#     message = models.CharField(max_length=255)
#     # relacja wiele do jednego (wiele komenatrzy może wskazywać jeden artykuł)
#     article = models.ForeignKey(Article, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.author + ":" + self.message

# class Comment(models.Model):
#
#     author = models.CharField(max_length=128)
#     message = models.CharField(max_length=255)
#     #relacja wiele do 1 (wiele komentarzy wskazuje na jeden artykuł)
#     article = models.ForeignKey(Article, on_delete=models.CASCADE)  #polaczenie obu modeli w relacji , do 1 artykułu wiele komentarzy(1 do wielu)
#     #jezeli ktos skasuje artykuł to tez komentarze do niego CASCADE


