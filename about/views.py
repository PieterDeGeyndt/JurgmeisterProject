from django.shortcuts import render
from .models import About

def about(request):
    services = About.objects
    return render(request,'about/about.html',{'services': services})

