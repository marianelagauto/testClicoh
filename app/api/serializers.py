from django.forms import ValidationError
from .models import Order, OrderDetail, Product
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetail
        fields = ('id', 'cuantity', 'product')
        extra_kwargs = {'id': {'read_only': False}}



class OrderSerializer(serializers.ModelSerializer):
    details = OrderDetailSerializer(many=True)

    class Meta:
        model = Order
        fields = ('date_time', 'get_total', 'get_total_usd', 'details')

    def create(self, validated_data):
        details = validated_data.pop('details')            
        errors = {'errors': []}
        # valida que no se repitan los productos
        products = [ detail['product'].id for detail in details]
        if len(set(products)) != len(products):
            errors['errors'] = {'order': 'La orden contiene productos repetidos'}

        for detail in details:  
            product = detail['product']
            try: 
                product.check_stock(detail['cuantity'])
            except ValidationError as e:
                errors['errors'].append({product.name: str(e)})

        if errors:
            raise serializers.ValidationError(errors)
        else:
            order = Order.objects.create(**validated_data)
            for detail in details: 
                product.decrease_stock(detail['cuantity'])
                product.save()
                OrderDetail.objects.create(order=order, **detail)
            
        return order

    def update(self, instance, validated_data):
        details_data = validated_data.pop('details')
        order_date_time = validated_data['date_time']
        details = instance.details.all()
        instance.date_time = order_date_time

        for detail_data in details_data:
            print(detail_data['id'])
            # si edita la cantidad del producto, hay que ver si aumenta o disminuye el stock
            # controlo y llamo a un metodo u otro?
            pass

        return instance


