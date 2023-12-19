# python version : 3.11.4
# Django : 5.0
from django.shortcuts import get_object_or_404
from django.http import JsonResponse, HttpResponse
from .models import Product_Data


def calculate_score(request):
    total_products = Product_Data.objects.count()
    # return HttpResponse(total_products)
    instock_products = Product_Data.objects.filter(stock='In Stock').count()
    
    availability_score = instock_products / total_products if total_products > 0 else 0
    
    return JsonResponse({'availability_score': availability_score})


def get_all_products(request):
    products = Product_Data.objects.all()
    # for product in products:
    #     return HttpResponse(product.meta_info.get('account_code'))
    #     exit
    total_products = Product_Data.objects.count()
    product_list = [{'id': product.id, 'stock': product.stock, 'score': product.available_price} for product in products]
    
    return JsonResponse({'products': product_list})
