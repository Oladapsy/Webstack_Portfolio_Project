from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClientViewSet, InvoiceViewSet, ItemViewSet

router = DefaultRouter()
router.register(r'clients', ClientViewSet)
router.register(r'invoices', InvoiceViewSet)
router.register(r'items', ItemViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]