from .models import Order, OrderDetail, Product
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class OrderDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderDetail
        fields = ('cuantity', 'product')


class OrderSerializer(serializers.ModelSerializer):
    details = OrderDetailSerializer(many=True)

    class Meta:
        model = Order
        fields = ('date_time', 'get_total', 'get_total_usd', 'details')

    def create(self, validated_data):
        details = validated_data.pop('details')            

        order = Order.objects.create(**validated_data)

        # validar que no se repitan los productos
        products = [ detail['product'].id for detail in details]
        if len(set(products)) != len(products):
            raise serializers.ValidationError({'message': 'La orden contiene productos repetidos'})

        for detail in details:  
            product = detail['product']
            try: 
                product.decrease_stock(detail['cuantity'])
                product.save()
                OrderDetail.objects.create(order=order, **detail)
            except Exception as e:
                error = {'message': str(e)}
                raise serializers.ValidationError(error)
            
        return order

    # def update(self, instance, validated_data):
    #     details_data = validated_data.pop('details')
    #     details = instance.details.all()
    #     print(instance)
    #     print(details_data)
    #     for detail_data in details_data:
    #         pass

    #     return instance


