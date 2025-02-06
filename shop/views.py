from django.shortcuts import render
from django.views.generic import ListView

from .models import Food

class HomeResturantListView(ListView):
    model = Food
    context_object_name = 'foods'
    template_name='Foods/shop_index.html'