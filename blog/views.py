from django.shortcuts import render
from .models import Post


def home(request):
    context = {'title': 'Home', 'posts': Post.objects.all()}
    return render(request, 'blog/home.html', context)


def about(request):
    context = {'title': 'About', 'posts': posts}
    return render(request, 'blog/about.html', context)
