from django.shortcuts import render,get_object_or_404
from .models import Abouts

def allabouts(request):
    abouts = Abouts.objects
    return render(request,'about/allabouts.html',{'abouts': abouts})

def aboutdetail(request, about_id):
    detailabout = get_object_or_404(Abouts, pk=about_id)
    return render(request,'about/detail.html', {'about': detailabout})