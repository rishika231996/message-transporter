from django.urls import path
from .views import calculate_score
from .views import get_all_products


urlpatterns = [
    path('score/', calculate_score, name='score'),
    path('products/', get_all_products, name='products'),
]