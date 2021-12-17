from django.urls import path
from . import views

urlpatterns = [
    path('',views.allcocktails, name='allcocktails'),
    path('<int:cocktail_id>/', views.detail, name='detail')
    ]