from django.conf import settings

from django.contrib.auth import get_user_model

from rest_framework.decorators import action
from rest_framework import viewsets, permissions, generics, filters, status

from apps.timesheet.models import PaymentHistory
from apps.timesheet.serializers import PaymentHistorySerializer

User = get_user_model()

__all__ = ("PaymentHistoryViewSet",)


class PaymentHistoryViewSet(viewsets.ModelViewSet):
    serializer_class = PaymentHistorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        current_user = self.request.user
        user = User.objects.filter(username=current_user)

        if current_user:
            queryset = PaymentHistory.objects.select_related("client").filter(
                client__user__in=user
            )
            return queryset

    # @action(methods=["post"], detail=False, serializer_class=PaymentHistorySerializer)
    # def checkout(self, *args, **kwargs):
