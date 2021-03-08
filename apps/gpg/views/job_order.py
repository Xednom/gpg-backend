from django.contrib.auth import get_user_model
from rest_framework import viewsets, permissions

from apps.authentication.models import Client, Staff
from apps.gpg.models import JobOrderGeneral
from apps.gpg.serializers import JobOrderGeneralSerializer

User = get_user_model()


class JobOrderGeneralViewSet(viewsets.ModelViewSet):
    serializer_class = JobOrderGeneralSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = "ticket_number"

    def get_queryset(self):
        job_order = JobOrderGeneral.objects.all()
        current_user = self.request.user
        clients = User.objects.filter(username=current_user)
        staffs = User.objects.filter(username=current_user)
        client = clients.all()
        staff = staffs.all()

        if staff:
            queryset = job_order.filter(client__user__in=client)
            return queryset
        elif client:
            queryset = job_order.filter(va_assigned__user__in=staff)
            return queryset
        elif current_user.is_superuser:
            queryset = JobOrderGeneral.objects.all()
            return queryset
