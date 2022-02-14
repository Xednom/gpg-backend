from django.shortcuts import render
from django.contrib.auth import get_user_model

from rest_framework import viewsets, permissions, generics, filters, status

from apps.account.models import LoginCredential, AccountFile
from apps.account.serializers import LoginCredentialSerializer, AccountFileSerializer

User = get_user_model()


class LoginCredentialViewSet(viewsets.ModelViewSet):
    serializer_class = LoginCredentialSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        current_user = self.request.user
        user = User.objects.filter(username=current_user)

        if current_user:
            queryset = LoginCredential.objects.prefetch_related("staff").filter(
                staff__user__in=user
            ) or LoginCredential.objects.select_related("client").filter(
                client__user__in=user
            )
            return queryset
        elif self.request.user.is_superuser:
            queryset = LoginCredential.objects.all()
            return queryset


class AccountFileViewSet(viewsets.ModelViewSet):
    serializer_class = AccountFileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        current_user = self.request.user
        user = User.objects.filter(username=current_user)

        if current_user:
            queryset = AccountFile.objects.prefetch_related("staff").filter(
                staff__user__in=user
            ) or AccountFile.objects.select_related("client").filter(
                client__user__in=user
            )
            return queryset
        elif self.request.user.is_superuser:
            queryset = AccountFile.objects.all()
            return queryset
