from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index_view(request):

    ctx = {}
    return render(request, 'index.html',ctx)

def home_view(request):

    ctx = {}
    return render(request, 'examples/profile-page.html',ctx)