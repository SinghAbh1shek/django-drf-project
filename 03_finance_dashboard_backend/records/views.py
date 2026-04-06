from rest_framework.viewsets import ModelViewSet
from .models import Record
from .serializers import RecordSerializer
from users.permissions import IsAdminAnalystOrOwner
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .filter import RecordFilter
from utils.paginator import StandardResultPagination


class RecordViewSet(ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    permission_classes = [IsAuthenticated, IsAdminAnalystOrOwner]
    filter_backends = (DjangoFilterBackend,)
    filterset_class = RecordFilter
    pagination_class = StandardResultPagination

    def get_queryset(self):
        user = self.request.user

        if user.role == 'admin':
            return Record.objects.all()

        if user.role == 'analyst':
            return Record.objects.all()

        if user.role == 'user':
            return Record.objects.filter(created_by=user)

        return Record.objects.none()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def perform_destroy(self, instance):
        instance.is_deleted = True
        instance.save()

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)