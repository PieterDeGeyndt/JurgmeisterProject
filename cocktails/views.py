from django.shortcuts import render

import cocktails
from .models import Cocktails

def allcocktails(request):
    cocktails=Cocktails.objects
    return render(request,'cocktails/allcocktails.html',{'cocktails': cocktails})