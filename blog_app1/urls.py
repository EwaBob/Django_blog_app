from django.urls import path

from blog_app1 import views

#
urlpatterns = [
    path('', views.blog_index),
    path('article/<int:pk>/', views.ShowArticle.as_view()),
    path('add/', views.AddArticle.as_view()),
]
# urlpatterns = [
#     path('article/add/', views.ArticleAdd.as_view()),
#     path('article/', views.article_list),
#     # path('article/<int:pk>/', views.blog_article_show),
#     path('article/<int:pk>', views.CommentAdd.as_view()),
#     ]