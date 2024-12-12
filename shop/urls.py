from django.urls import path
from .views import ProductsListView, ProductDetailView, chat_message

urlpatterns = [
    path('', ProductsListView.as_view(), name='products-list'),
    path('product/<slug:slug>/<int:id>/', ProductDetailView.as_view(), name='product-detail'),
    path('chat/', chat_message, name='chat-message')
]