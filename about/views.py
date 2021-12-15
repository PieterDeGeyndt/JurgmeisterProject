from django.shortcuts import render
from .models import About

def home(request):
    services = About.objects
    return render(request,'about/home.html',{'services': services})

