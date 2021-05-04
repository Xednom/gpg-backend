from django.conf import settings

from django.contrib.auth import get_user_model
from rest_framework import viewsets, permissions, generics, filters, status

from apps.timesheet.models import StaffAccountBalance
from apps.timesheet.serializers import StaffAccountBalanceSerializer

User = get_user_model()


__all__=("StaffAccountBalanceViewSet",)


class StaffAccountBalanceViewSet(viewsets.ModelViewSet):
    serializer_class = StaffAccountBalanceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        current_user = self.request.user
        user = User.objects.filter(username=current_user)

        if current_user:
            queryset = StaffAccountBalance.objects.select_related("staff").filter(
                staff__user__in=user
            )
            return queryset
        return queryset