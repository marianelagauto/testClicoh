from django.db import models
from django.db.models import Sum
from django.forms import ValidationError
from django.core.validators import MinValueValidator 
import requests

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    stock = models.IntegerField(default=0)

    def check_stock(self, cuantity):
        if self.stock < cuantity:
            raise ValidationError("El stock no es suficiente",code="invalid")

    def decrease_stock(self, cuantity):
        self.stock = self.stock - cuantity

    def restore_stock(self, cuantity):
        # entiendo que aca no es necesario ver si cuantity > 0
        self.stock = self.stock + cuantity

    def __str__(self):
        return self.name


class Order(models.Model):
    date_time = models.DateTimeField()

    @property
    def get_total(self):
        return OrderDetail.objects.filter(order=self).aggregate(Sum('product__price'))['product__price__sum']

    @property
    def get_total_usd(self):
        response = requests.get('https://www.dolarsi.com/api/api.php?type=valoresprincipales')
        value = response.json()[1]['casa']['compra']
        dolar_value = value.replace(",", ".")
        return self.get_total * float(dolar_value)


class OrderDetail(models.Model):
    order = models.ForeignKey(Order,related_name="details", on_delete=models.CASCADE)
    cuantity = models.IntegerField(validators=[MinValueValidator(1)])
    product = models.ForeignKey(Product, on_delete=models.CASCADE)