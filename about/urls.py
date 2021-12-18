from django.urls import path
from . import views

urlpatterns = [
    path('',views.allabouts, name='allabouts'),
    path('<int:about_id>/', views.aboutdetail, name='aboutdetail')
    ]