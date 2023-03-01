"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include


urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('', views.main),
    # path('hello/', views.hello),
    # path('add/', views.add),
    # path('brothers/', views.brothers),
    # path('fibonnaci/', views.fibonnaci),
    # path('multiply/', views.multiply),
    # path('game/', views.game),
    # path('article/<int:id>/', views.article),
    # path('greetings/<str:name>/<int:repeat>/', views.greetings),
    # path('calc/<str:number_a>/<str:operation>/<str:number_b>/', views.calc),
    # path('random_generator/<int:min>/<int:max>/', views.random_generator),
    # path('random_generator/<int:min>/<int:max>/<int:throw>', views.random_generator),
    # path('abc/', views.show_template),
    # path('template/', views.first_template),
    # path('fizz/', views.fizz_buzz),
    # path('tab/', views.multiply1),
    # path('form/', views.show_form),
    # path('login/', views.login_user),
    # path('addproduct/', views.add_product),
    # path('product_show/', views.product_show),
    # path('class/', views.FormView.as_view()),
    # path('test/', views.TestView.as_view()),
    # path('testshow/', views.ShowTestView.as_view()),
    # path('pizza/', views.PizzaView.as_view()),
    # path('car/', views.CarView.as_view()),
    # path('login_class/', views.LoginView.as_view()),
    # path('book/add/', views.BookAdd.as_view()),
    # path('book/', views.book_list),
    # path('book/edit/<int:pk>', views.BookEdit.as_view()),
    # path('book/delete/<int:pk>', views.BookDelete.as_view()),
    # path('article/add/', views.AddArticle.as_view()),
    # path('article/', views.article_list),
    # # path('article/<int:pk>/', views.blog_article_show),
    # path('article/<int:pk>/', views.CommentAdd.as_view()),
    path('blog/', include('blog_app1.urls'))

]

#include przekierowanie do naszego nowego pliku


