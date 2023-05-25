from django.shortcuts import render
from django.views import View
from .models import Recipe, Category
import random


class MainView(View):
    def get(self, request):
        recipes = random.sample(list(Recipe.objects.all()), 10)
        return render(request, 'main.html', {'recipes': recipes})


class CategoryDetailView(View):
    def get(self, request, category_id):
        category = Category.objects.get(id=category_id)
        recipes = Recipe.objects.filter(category=category)
        return render(request, 'category_detail.html', {'category': category, 'recipes': recipes})
