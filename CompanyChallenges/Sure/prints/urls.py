from django.urls import path
from .views import PrintsView


urlpatterns = [
    path('prints/', PrintsView.as_view(), name="prints-all"),
]