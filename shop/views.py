from django.db.models import Count
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Category, Product, ProductAttribute
# Create your views here.
#
# def home(request):
#     categories = Category.objects.all().annotate(product_count=Count('children__products__attributes')).filter(parent__isnull=True)
#     product_attributes = ProductAttribute.objects.all().select_related('product', 'color', 'size').prefetch_related('images').order_by('?')
#     context = {
#         'categories': categories,
#         'products': product_attributes
#     }
#     return render(request, 'shop-grid.html', context)

class ProductsListView(ListView):
    model = ProductAttribute
    template_name = 'shop-grid.html'
    context_object_name = 'products'
    paginate_by = 15

    def get_queryset(self):
        return ProductAttribute.objects.all().select_related('product', 'color', 'size').prefetch_related('images').order_by('?')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all().annotate(product_count=Count('children__products__attributes')).filter(parent__isnull=True)
        return context


class ProductDetailView(DetailView):
    model = ProductAttribute
    template_name = 'shop-product-detail.html'
    context_object_name = 'product'

    def get_object(self, queryset=None):
        return ProductAttribute.objects.get(product__slug=self.kwargs['slug'], id=self.kwargs['id'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all().annotate(product_count=Count('children__products__attributes')).filter(parent__isnull=True)
        context['related_products'] = ProductAttribute.objects.filter(product__category=context['product'].product.category).exclude(id=context['product'].id).select_related('product', 'color', 'size').prefetch_related('images').order_by('?')[:4]
        return context


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def chat_message(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_message = data.get('message', '')

            reply = f"Sizning xabaringiz: {user_message}"

            products = [
                {
                    "category": "Erkaklar Kiyimlar",
                    "name": "Oversize Klassik Ko'ylak",
                    "price": 230000,
                    "color": "Qora",
                    "status": "SALE",
                    "image": "http://127.0.0.1:8000/media/product/images/cr30c8usbq7g1s9a7o4g.jpg",
                    "slug": "oversize-klassik-koylak",
                    "attr_id": 2
                },
                {
                    "category": "Ayollar Kiyimlar",
                    "name": "Oversize  Ko'ylak",
                    "price": 200000,
                    "color": "Oq",
                    "status": "NEW",
                    "image": "http://127.0.0.1:8000/media/product/images/cr30d77iraat934qcedg_vN6pw2c.jpg",
                    "slug": "oversize-koylak",
                    "attr_id": 8
                },

            ]

            search_filter = {
                "category_ids": [2,4,5],
                "color_ids": [1,2,3],
                "size": [2,4],
                "price": [100000, 500000],
                "search": "Kiyim"

            }

            return JsonResponse({'reply': reply, 'products': products, 'search_filter': search_filter})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': 'Invalid request method'}, status=400)
