from django.test import TestCase, Client
from django.urls import reverse
from .models import Recipe, Category

# Create your tests here.
class RecipeViewsTestCase(TestCase):
    def setUp(self):
        # Set up any necessary data for the tests, such as creating recipes and categories.
        # For example:
        self.category = Category.objects.create(name='Dessert')
        self.recipe1 = Recipe.objects.create(title='Chocolate Cake', category=self.category)
        self.recipe2 = Recipe.objects.create(title='Apple Pie', category=self.category)

    def test_main_view(self):
        # Test the main view that displays 10 random recipes.
        client = Client()
        response = client.get(reverse('recipe:main'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main.html')
        # Add more specific assertions to check the content of the response.

    def test_category_detail_view(self):
        # Test the category_detail view that displays recipes of a specific category.
        client = Client()
        category_id = self.category.id
        response = client.get(reverse('recipe:category_detail', args=[category_id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'category_detail.html')
        # Add more specific assertions to check the content of the response.
