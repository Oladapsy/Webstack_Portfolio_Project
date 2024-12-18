from rest_framework import viewsets
from .models import UnifiedModel
from .serializers import UnifiedModelSerializer
from rest_framework.permissions import IsAuthenticated

class UnifiedModelViewSet(viewsets.ModelViewSet):
    queryset = UnifiedModel.objects.all()
    serializer_class = UnifiedModelSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)  # Filter invoices by authenticated user

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
