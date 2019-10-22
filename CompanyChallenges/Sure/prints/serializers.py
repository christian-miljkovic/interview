from rest_framework import serializers
from .models import Prints


class PrintsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prints
        fields = ("size", "cost", "shipping_cost", "total_cost")