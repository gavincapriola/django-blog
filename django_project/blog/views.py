from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Post


def index(request):
    return render(request, 'blog/index.html', {'posts': Post.objects.all()})


class PostListView(ListView):
    model = Post
    template_name = 'blog/index.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-created_date']


class PostDetailView(DetailView):
    model = Post


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
