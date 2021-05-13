from django.contrib.auth import get_user_model
from django.db.models import query

from django.shortcuts import render
from apps.due_diligence import serializers
from rest_framework import viewsets, permissions

from apps.authentication.models import Staff
from apps.due_diligence.models import PhoneLineExtension
from apps.due_diligence.serializers import PhoneLineExtSerializer

User = get_user_model()


class PhoneLineExtViewSet(viewsets.ModelViewSet):
    serializer_class = PhoneLineExtSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        current_user = self.request.user
        staffs = User.objects.filter(username=current_user)
        staff = staffs.all()

        if staffs:
            queryset = PhoneLineExtension.objects.prefetch_related(
                "allocated_extension_staff"
            ).filter(allocated_extension_staff__user__in=staff)
            return queryset
