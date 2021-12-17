from django.shortcuts import render,get_object_or_404
from .models import Cocktails


def allcocktails(request):
    cocktails=Cocktails.objects
    return render(request,'cocktails/allcocktails.html',{'cocktails': cocktails})

def detail(request, cocktail_id):
    detailcocktail = get_object_or_404(Cocktails, pk=cocktail_id)
    return render(request,'cocktails/detail.html', {'cocktail': detailcocktail})