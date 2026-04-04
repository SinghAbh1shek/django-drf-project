from rest_framework.viewsets import ModelViewSet
from .models import Record
from .serializers import RecordSerializer
from users.permissions import IsAdminOrAnalyst
from rest_framework.permissions import IsAuthenticated


class RecordViewSet(ModelViewSet):
    queryset = Record.objects.filter(is_deleted=False)
    serializer_class = RecordSerializer
    permission_classes = [IsAuthenticated, IsAdminOrAnalyst]

    def perform_create(self, serializer):
        print(self.request.user)
        print(self.request.user.role)
        serializer.save(created_by=self.request.user)

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)