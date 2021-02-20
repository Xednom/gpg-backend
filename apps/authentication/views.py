from rest_framework import viewsets, permissions

from .models import Staff, Client
from .serializers import StaffSerializer, ClientSerializer


class StaffViewSet(viewsets.ModelViewSet):
    serializer_class = StaffSerializer
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    queryset = Staff.objects.all()


class ClientViewSet(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    permission_classes = [
        permissions.IsAuthenticated
    ]
    queryset = Client.objects.all()