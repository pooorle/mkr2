from django.contrib import admin
from django.urls import path
from recipe.views import MainView, CategoryDetailView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainView.as_view(), name='main'),
    path('category/<int:category_id>/', CategoryDetailView.as_view(), name='category_detail'),
]