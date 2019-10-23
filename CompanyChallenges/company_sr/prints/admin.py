from django.contrib import admin
from .models import Prints, Order, Photo
from django.shortcuts import redirect

admin.site.register(Prints)
admin.site.register(Order)
admin.site.register(Photo)