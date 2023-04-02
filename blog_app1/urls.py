from django.urls import path

from blog_app1 import views

#
urlpatterns = [
    path('', views.blog_index),
    path('article/<int:pk>/', views.ShowArticle.as_view()),
    path('add/', views.AddArticle.as_view()),
