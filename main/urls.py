from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import ProductListCreateAPIView, ProductRetrieveUpdateDestroyAPIView, MyView

urlpatterns = [
    path('products/', ProductListCreateAPIView.as_view(), name='product-list-create'),
    path('products/aza/', ProductRetrieveUpdateDestroyAPIView.as_view(), name='product-detail'),
    path('MyView1/', login_required(MyView.as_view()))
]


