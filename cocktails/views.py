from django.shortcuts import render

import cocktails
from .models import Cocktails

def allcocktails(request):
    return render(request,'cocktails/allcocktails.html',{'cocktails': cocktails})