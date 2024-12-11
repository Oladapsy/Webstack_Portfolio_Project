from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UnifiedModelViewSet

router = DefaultRouter()
router.register(r'unified', UnifiedModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
