from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    stock = models.IntegerField(default=0)


class Order(models.Model):
    date_time = models.DateTimeField()


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    cuantity = models.IntegerField(default=0)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)