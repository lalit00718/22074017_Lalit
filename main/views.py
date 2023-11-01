from django.shortcuts import render, redirect
from django.urls import reverse
from .models import LinkMapping
from . import service

# Create your views here.

def index(request):
    return render(request, 'main/index.html')

def redirect_hash(request, url_hash):
    original_url = service.load_url(url_hash).original_url
    return redirect(original_url)

def shorten_post(request):
    return shorten(request, request.POST['url'])

def shorten(request, url):
    shortened_url_hash = service.shorten(url)
    shortened_url = request.build_absolute_uri(reverse('redirect', args=[shortened_url_hash]))
    return render(request, 'main/link.html', {'shortened_url': shortened_url})

def short(request):
    urls = LinkMapping.objects.all()
    return render(request, "main/all.html", {'urls':urls})