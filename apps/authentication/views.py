from django.contrib.auth import get_user_model
from rest_framework import viewsets, permissions

from .models import Staff, Client
from .serializers import StaffSerializer, ClientSerializer

User = get_user_model()


class StaffViewSet(viewsets.ModelViewSet):
    serializer_class = StaffSerializer
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def get_queryset(self):
        current_user = self.request.user
        staff = Staff.objects.all()
        
        if current_user:
            qs = staff.filter(user=current_user)
            return qs


class ClientViewSet(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    lookup_field = "user"
    permission_classes = [
        permissions.IsAuthenticated
    ]
    
    def get_queryset(self):
        current_user = self.request.user
        client = Client.objects.all()

        if current_user:
            qs = client.filter(user=current_user)
            return qs