from itertools import product
from django import views
from django.shortcuts import render
from .models import Product
from .serializers import OrderDetailSerializer, OrderSerializer, ProductSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = ProductSerializer.Meta.model.objects.all()


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = OrderSerializer.Meta.model.objects.all()

    def destroy(self, request, pk=None, *args, **kwargs):
        instance = self.get_object()
        for detail in instance.details.all():
            print(detail.product)

        return super(OrderViewSet, self).destroy(request, pk, *args, **kwargs)


class OrderDetailViewSet(viewsets.ModelViewSet):
    serializer_class = OrderDetailSerializer
    queryset = OrderDetailSerializer.Meta.model.objects.all()