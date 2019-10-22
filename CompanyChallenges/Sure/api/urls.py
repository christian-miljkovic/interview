from django.contrib import admin
from django.urls import path, re_path, include
from django.urls import path

# from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('api/(?P<version>(v1|v2))/', include('prints.urls')),
    path('', include('prints.urls')),
]