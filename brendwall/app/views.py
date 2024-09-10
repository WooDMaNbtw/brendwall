from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .models import Product
from .serializers import ProductSerializer


class ProductView(ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


def main(request):
    return render(request, 'main.html')