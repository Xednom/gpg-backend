from django.contrib.auth import get_user_model
from rest_framework import viewsets, permissions, filters, generics
from djoser.email import ConfirmationEmail, PasswordResetEmail

from .models import Staff, Client, InternalFiles, InternalFilesStaff
from .serializers import (
    StaffSerializer,
    ClientSerializer,
    ClientInternalFileSerializer,
    StaffInternalFileSerializer,
    ClientCodeSerializer,
    StaffCodeSerializer,
)

User = get_user_model()


class StaffViewSet(viewsets.ModelViewSet):
    serializer_class = StaffSerializer
    lookup_field = "user"
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    queryset = Staff.objects.all()


class ClientViewSet(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    lookup_field = "user"
    permission_classes = [permissions.IsAuthenticated]
    queryset = Client.objects.all()


class ClientCodeViewSet(viewsets.ModelViewSet):
    serializer_class = ClientCodeSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Client.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ["=client_code"]


class StaffViewSet(viewsets.ModelViewSet):
    serializer_class = StaffSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Staff.objects.all()


class ClientFilesViewSet(viewsets.ModelViewSet):
    serializer_class = ClientInternalFileSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = InternalFiles.objects.all()

    def get_queryset(self):
        current_user = self.request.user
        client = InternalFiles.objects.all()

        if current_user:
            qs = InternalFiles.objects.filter(client__user=current_user)
            return qs


class StaffFilesViewSet(viewsets.ModelViewSet):
    serializer_class = StaffInternalFileSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = InternalFilesStaff.objects.all()

    def get_queryset(self):
        current_user = self.request.user
        client = InternalFilesStaff.objects.all()

        if current_user:
            qs = InternalFilesStaff.objects.filter(staff__user=current_user)
            return qs


class StaffCodeList(generics.ListAPIView):
    serializer_class = StaffCodeSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Staff.objects.all()


class GpgConfirmationEmail(ConfirmationEmail):
    template_name = "email/confirmation_email.html"


class GpgPasswordResetEmail(PasswordResetEmail):
    template_name = "email/forgot_password_email.html"
