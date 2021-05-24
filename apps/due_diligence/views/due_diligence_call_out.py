from django.contrib.auth import get_user_model
from django.db.models import query, Q

from django.shortcuts import render
from apps.due_diligence import serializers
from rest_framework import viewsets, permissions

from apps.authentication.models import Staff
from apps.due_diligence.models import DueDiligenceCallOut
from apps.due_diligence.serializers import CallOutSerializer

User = get_user_model()


class CallOutViewSet(viewsets.ModelViewSet):
    serializer_class = CallOutSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = "id"

    def get_queryset(self):
        current_user = self.request.user
        user = User.objects.filter(username=current_user)
        user = user.all()

        if user:
            queryset = (
                DueDiligenceCallOut.objects.prefetch_related(
                    "staff_initial_dd", "staff_assigned_for_call_out"
                ).filter(Q(
                    staff_initial_dd__user__in=user) |
                    Q(staff_assigned_for_call_out__user__in=user)
                )
                or DueDiligenceCallOut.objects.select_related("client").filter(
                    client__user__in=user
                )
            )
            return queryset
