from django.forms import ValidationError
from .models import Order, OrderDetail, Product
from rest_framework import serializers


def check_repeated_products(details, errors):
    products = [ detail['product'].id for detail in details]
    if len(set(products)) != len(products):
        return True


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetail
        fields = ('id', 'cuantity', 'product')


class OrderDetailWithIdSerializer(serializers.ModelSerializer):
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
        if check_repeated_products(details, errors):
            errors['errors'] = {'order': 'La orden contiene productos repetidos'}

        for detail in details:  
            product = detail['product']
            try: 
                product.check_stock(detail['cuantity'])
            except ValidationError as e:
                errors['errors'].append({product.name: str(e)})

        if errors['errors']:
            raise serializers.ValidationError(errors)
        else:
            order = Order.objects.create(**validated_data)
            for detail in details: 
                detail['product'].decrease_stock(detail['cuantity'])
                detail['product'].save()
                OrderDetail.objects.create(order=order, **detail)
        return order


class OrderUpdateSerializer(serializers.ModelSerializer):
    details = OrderDetailWithIdSerializer(many=True)

    class Meta:
        model = Order
        fields = ('date_time', 'details')
        
    def update(self, instance, validated_data):
        errors = {'errors': []}
        details_data = validated_data.pop('details')
        details = instance.details.all()

        if check_repeated_products(details_data, errors):
            errors['errors'] = {'order': 'La orden contiene productos repetidos'}

        for detail_data in details_data:
            detail = details.filter(id=detail_data['id']).get()
            if detail_data['cuantity'] > detail.cuantity:
                try: 
                    detail.product.check_stock(detail_data['cuantity'])
                except ValidationError as e:
                    errors['errors'].append({detail.product.name: str(e)})

        if errors['errors']:
            raise serializers.ValidationError(errors)
        else:
            instance.date_time = validated_data['date_time']
            for detail_data in details_data:
                detail = details.filter(id=detail_data['id']).get()
                detail.product = detail_data['product'] 
                if detail_data['cuantity'] > detail.cuantity:
                    detail.product.decrease_stock(detail_data['cuantity'])
                elif detail_data['cuantity'] < detail.cuantity:
                    detail.product.restore_stock(detail.cuantity - detail_data['cuantity'])
                detail.product.save()
        return instance

    


