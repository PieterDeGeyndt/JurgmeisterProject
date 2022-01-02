from django.urls import path
from . import views
from .views import add_to_cart
from .views import remove_from_cart

urlpatterns = [
    path('',views.allcocktails, name='allcocktails'),
    path('<int:cocktail_id>/', views.detail, name='detail'),
    path('add-to-cart/<int:cocktail_id>/', add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<int:cocktail_id>/', remove_from_cart, name='remove-from-cart'),
    ]