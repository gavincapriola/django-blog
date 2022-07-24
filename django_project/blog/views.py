from django.shortcuts import render

posts = [
    {
        'author': 'John Doe',
        'title': 'Blog Post One',
        'body': 'first',
        'created_date': 'July 23, 2022'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post Two',
        'body': 'second',
        'created_date': 'July 23, 2022'
    }
]


def index(request):
    return render(request, 'blog/index.html', {'posts': posts})


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
