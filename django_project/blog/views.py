from django.shortcuts import render

from .models import Post


def index(request):
    return render(request, 'blog/index.html', {'posts': Post.objects.all()})


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
