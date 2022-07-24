from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Hello, world. You're at the blog home.")


def about(request):
    return HttpResponse("This is the about page.")
