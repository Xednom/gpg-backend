from django.conf import settings

from django.contrib.auth import get_user_model
from rest_framework import viewsets, permissions, generics, filters, status

from apps.timesheet.models import AccountBalance
from apps.timesheet.serializers import AccountBalanceSerializer

User = get_user_model()


__all__=("AccountBalanceViewSet",)


class AccountBalanceViewSet(viewsets.ModelViewSet):
    serializer_class = AccountBalanceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        current_user = self.request.user
        user = User.objects.filter(username=current_user)

        if current_user:
            queryset = AccountBalance.objects.select_related("client").filter(
                client__user__in=user
            )
            return queryset
        return queryset