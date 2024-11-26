from rest_framework import serializers
from .models import Order,Product,User

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class OrderSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Order
        fields = "__all__"