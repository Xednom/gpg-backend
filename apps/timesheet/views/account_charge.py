from django.conf import settings

from django.contrib.auth import get_user_model
from rest_framework import viewsets, permissions, generics, filters, status

from apps.timesheet.models import AccountCharge
from apps.timesheet.serializers import AccountChargeSerializer

User = get_user_model()

__all__ = ("AccountChargeViewSet",)


class AccountChargeViewSet(viewsets.ModelViewSet):
    serializer_class = AccountChargeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        current_user = self.request.user
        user = User.objects.filter(username=current_user)

        if current_user:
            queryset = AccountCharge.objects.select_related("client", "staff").filter(
                client__user__in=user
            ) or AccountCharge.objects.select_related("client", "staff").filter(
                staff__user__in=user
            )
            return queryset
