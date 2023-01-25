from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import Order

class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'