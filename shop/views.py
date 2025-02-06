from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Food


class HomeResturantListView(ListView):
    model = Food
    context_object_name = "foods"
    template_name = "Foods/Shop_index.html"


class ProductDetailView(DetailView):
    model = Food
    context_object_name='food'
    template_name = "foods/Shop_detail.html"
