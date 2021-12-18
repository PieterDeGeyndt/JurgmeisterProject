from django.shortcuts import render,get_object_or_404
from .models import Abouts

def allabouts(request):
    abouts = Abouts.objects
    return render(request,'abouts/allabouts.html',{'abouts': abouts})

def detail(request, about_id):
    detailabout = get_object_or_404(Abouts, pk=about_id)
    return render(request,'abouts/detail.html', {'about': detailabout})