from rest_framework import serializers
from .models import Prints, Order, Photo


class PrintsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prints
        fields = ("size", "cost", "shipping_cost", "total_cost")


class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ("first_name", "last_name", "email", "phone_number", "address_one",
                    "address_two", "city", "state", "postal_code", "country")

class PhotosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ("name", "image")