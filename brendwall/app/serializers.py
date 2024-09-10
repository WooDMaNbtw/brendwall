from rest_framework.exceptions import ParseError
from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'title', 'description', 'price')

        """
        neglecting additional validation
        
        extra_kwargs = {
            'title': {'required': True},
            'description': {'required': True},
            'price': {'required': True, 'max_digits': 10, 'decimal_places': 2},
        }
        """

    def validate(self, attrs):
        title = attrs.get('title')
        price = attrs.get('price')


        if not title:
            raise ParseError(detail="Title is required.")

        if not price:
            raise ParseError(detail="Price is required.")

        if price < 0:
            raise ParseError(detail="Price cannot be negative.")

        return attrs
