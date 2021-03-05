from django.contrib.auth import get_user_model
from rest_framework import viewsets, permissions

from .models import Staff, Client, InternalFiles, InternalFilesStaff
from .serializers import StaffSerializer, ClientSerializer, ClientInternalFileSerializer, StaffInternalFileSerializer

User = get_user_model()


class StaffViewSet(viewsets.ModelViewSet):
    serializer_class = StaffSerializer
    lookup_field = "user"
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def get_queryset(self):
        current_user = self.request.user
        staff = Staff.objects.all()
        
        if current_user:
            qs = staff.filter(user__username=current_user)
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
            qs = client.filter(user__username=current_user)
            return qs


class ClientFilesViewSet(viewsets.ModelViewSet):
    serializer_class = ClientInternalFileSerializer
    permission_classes = [
        permissions.IsAuthenticated
    ]
    queryset = InternalFiles.objects.all()

    def get_queryset(self):
        current_user = self.request.user
        client = InternalFiles.objects.all()

        if current_user:
            qs = InternalFiles.objects.filter(client__user=current_user)
            return qs


class StaffFilesViewSet(viewsets.ModelViewSet):
    serializer_class = StaffInternalFileSerializer
    permission_classes = [
        permissions.IsAuthenticated
    ]
    queryset = InternalFilesStaff.objects.all()

    def get_queryset(self):
        current_user = self.request.user
        client = InternalFilesStaff.objects.all()

        if current_user:
            qs = InternalFilesStaff.objects.filter(staff__user=current_user)
            return qs