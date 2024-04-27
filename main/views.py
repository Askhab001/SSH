from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class MyView(LoginRequiredMixin, View):
    @login_required
    def my_view(request):
        return HttpResponse('Авторизованный пользователь')

