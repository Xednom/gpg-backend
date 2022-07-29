import datetime

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
    lookup_field = "id"

    def get_queryset(self):
        current_user = self.request.user
        user = User.objects.filter(username=current_user)
        today = datetime.date.today()

        if current_user:
            queryset = AccountCharge.objects.select_related("client", "staff").filter(
                client__user__in=user
            ).exclude(status="submitted") or AccountCharge.objects.select_related(
                "client", "staff"
            ).filter(
                staff__user__in=user,
                shift_date__month=today.month,
                shift_date__year=today.year,
            )
            return queryset
