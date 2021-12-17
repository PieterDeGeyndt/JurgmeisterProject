from django.shortcuts import render
from .models import Homepage

def home(request):
    homepage=Homepage.objects
    return render(request,'homepage/home.html',{'homepage':homepage})
