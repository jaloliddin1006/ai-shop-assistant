from django.urls import path
from .views import ProductsListView, ProductDetailView

urlpatterns = [
    path('', ProductsListView.as_view(), name='products-list'),
    path('product/<slug:slug>/<int:id>/', ProductDetailView.as_view(), name='product-detail')
]