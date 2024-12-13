from django.urls import path

from shop.rasa_view import get_products, rasa_query
from .views import ProductsListView, ProductDetailView, chat_message

urlpatterns = [
    path('', ProductsListView.as_view(), name='products-list'),
    path('product/<slug:slug>/<int:id>/', ProductDetailView.as_view(), name='product-detail'),
    path('chat/', chat_message, name='chat-message'),
       path('api/products/', get_products, name='get_products'),
     path('rasa-query/', rasa_query, name='rasa_query'),
]