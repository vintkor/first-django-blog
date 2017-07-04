from django.shortcuts import render
from .models import Article


def blog(request):
    article_list = Article.articles.filter().order_by('-pub_date')
    context = {'article_list': article_list}

    return render(request, 'blog/index.html', context)
