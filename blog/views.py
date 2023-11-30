# views.py
from django.shortcuts import get_object_or_404, render
from .models import Article, Profile, Tag
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm


def registerPage(request):
    form = CreateUserForm
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'register2.html', context)


def loginPage(request):
    context = {}
    return render(request, 'login.html')


def home(request):
    featured = Article.articlemanager.filter(featured=True)[0:3]
    context = {
        'articles': featured
    }
    return render(request, 'index.html', context)


def article(request, article):
    article = get_object_or_404(Article, slug=article, status='published')
    context = {
        'article': article
    }
    return render(request, 'article.html', context)


def articles(request):
    query = request.GET.get('query', '')  # get query from request

    articles = Article.articlemanager.filter(
        Q(headline__icontains=query) |  # search for query in headline, sub headline, body
        Q(sub_headline__icontains=query) |
        Q(body__icontains=query)
    )

    tags = Tag.objects.all()
    context = {
        'articles': articles,
        'tags': tags,
    }
    return render(request, 'articles.html', context)
