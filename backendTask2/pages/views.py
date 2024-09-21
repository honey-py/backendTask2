from django.http import HttpResponse
from django.shortcuts import render

def home_view(request, *args, **kwargs):
    return render(request, 'index.html', {})

def content1(request, *args, **kwargs):
    return render(request, 'content1.html', {})

def content2(request, *args, **kwargs):
    return render(request, 'content2.html', {})

def content3(request, *args, **kwargs):
    return render(request, 'content3.html', {})