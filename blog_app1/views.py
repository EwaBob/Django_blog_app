from django.shortcuts import render, redirect
from django.views import View

from blog_app1.models import Article, Comment

def blog_index(request):
    return render(request, "blog_app/index.html",
                  {"articles": Article.objects.all()})

class ShowArticle(View):
    def get(self, request, pk):
        article = Article.objects.get(pk=pk)
        return render(request, "blog_app/show_article.html",
                      {"article": article})

    def post(self, request, pk):
        article = Article.objects.get(pk=pk)
        author = request.POST.get("author")
        message = request.POST.get("message")

        Comment.objects.create(author=author, message=message, article=article)
        return redirect(f"/blog/article/{pk}")

class AddArticle(View):
    def get(self, request):
        return render(request, "blog_app/article_add.html")

    def post(self, request):
        title = request.POST.get("title")
        description = request.POST.get("description")

        Article.objects.create(title=title, description=description)
        return redirect("/blog/")