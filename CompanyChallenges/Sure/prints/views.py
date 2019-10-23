from django.shortcuts import render
from rest_framework import generics
from .models import Prints, Order, Photo
from .serializers import PrintsSerializer, OrdersSerializer, PhotosSerializer


class PrintsView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Prints.objects.all()
    serializer_class = PrintsSerializer

class OrdersView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Order.objects.all()
    serializer_class = OrdersSerializer

class PhotosView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Photo.objects.all()
    serializer_class = PhotosSerializer
