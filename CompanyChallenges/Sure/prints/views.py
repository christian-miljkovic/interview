from django.shortcuts import render
from rest_framework import generics
from .models import Prints
from .serializers import PrintsSerializer


class PrintsView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Prints.objects.all()
    serializer_class = PrintsSerializer
