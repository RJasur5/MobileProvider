from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'company', 'duedate']

    def create(self, validated_data):
        return Product.objects.create(validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.price = validated_data.get('price', instance.price)
        instance.company = validated_data.get('company', instance.company)
        instance.duedate = validated_data.get('duedate', instance.duedate)
        instance.save()
        return instance
