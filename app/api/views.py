from django.shortcuts import render
from .models import Product
from .serializers import OrderSerializer, ProductSerializer
from rest_framework import viewsets


class ProductViewSet(viewsets.ModelViewSet):
    """  """
    serializer_class = ProductSerializer
    queryset = ProductSerializer.Meta.model.objects.all()


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = OrderSerializer.Meta.model.objects.all()