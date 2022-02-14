from django.conf import settings

from rest_framework import viewsets, permissions, generics, filters, status

from apps.timesheet.models import PaymentPortal
from apps.timesheet.serializers import PaymentPortalSerializer

__all__ = ("PaymentPortalViewSet",)


class PaymentPortalViewSet(viewsets.ModelViewSet):
    serializer_class = PaymentPortalSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = PaymentPortal.objects.all()
