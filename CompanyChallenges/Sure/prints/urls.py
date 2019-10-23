from django.urls import path
from .views import PrintsView, OrdersView, PhotosView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('prints/', PrintsView.as_view(), name="prints-all"),
    path('orders/', OrdersView.as_view(), name="orders-all"),
    path('photos/', PhotosView.as_view(), name="orders-all"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)