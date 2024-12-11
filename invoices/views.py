from rest_framework import viewsets
from .models import UnifiedModel
from .serializers import UnifiedModelSerializer
from rest_framework.permissions import IsAuthenticated

class UnifiedModelViewSet(viewsets.ModelViewSet):
    queryset = UnifiedModel.objects.all()
    serializer_class = UnifiedModelSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
