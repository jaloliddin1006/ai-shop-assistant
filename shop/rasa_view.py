from django.http import JsonResponse
from shop.models import RasaProduct

# def get_products(request):
#     category = request.GET.get('category', '')
#     color = request.GET.get('color', '')
#     material = request.GET.get('material', '')

#     products = RasaProduct.objects.filter(
#         name__icontains=category,
#         color__icontains=color,
#         material__icontains=material
#     )
#     data = list(products.values('id', 'name', 'color', 'size', 'price', 'quantity'))
#     return JsonResponse({'products': data})


import requests
from django.http import JsonResponse

def rasa_query(request):
    message = request.GET.get('message', '')
    rasa_url = "http://localhost:5005/webhooks/rest/webhook"
    
    payload = {
        "sender": "django_user",
        "message": message
    }
    response = requests.post(rasa_url, json=payload)
    bot_response = response.json()

    return JsonResponse(bot_response, safe=False)


# views.py

from django.http import JsonResponse
from .models import RasaProduct

def get_products(request):
    query = request.GET.get('query', '')
    products = RasaProduct.objects.filter(name__icontains=query)
    products_data = [{"name": p.name, "price": p.price} for p in products]
    return JsonResponse({"products": products_data})
