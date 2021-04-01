from django.contrib.auth import get_user_model
from rest_framework import viewsets, permissions, generics
from rest_framework.generics import get_object_or_404

from apps.authentication.models import Client, Staff
from apps.gpg.models import JobOrderGeneral, Comment
from apps.gpg.serializers import JobOrderGeneralSerializer, CommentSerializer
from apps.gpg.notifications.email import JobOrderGeneralEmail, JobOrderCommentEmail

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

        if current_user:
            queryset = job_order.filter(client__user__in=client) or job_order.filter(
                va_assigned__user__in=staff
            ).select_related("client", "va_assigned")
            return queryset
        elif current_user.is_superuser:
            queryset = JobOrderGeneral.objects.all()
            return queryset

    def perform_update(self, serializer):
        instance = self.get_object()
        ticket_number = instance.ticket_number
        client_email = instance.client_email
        staff_email = instance.staff_email
        job_order = serializer.validated_data
        JobOrderGeneralEmail(ticket_number, job_order, client_email, staff_email).send()
        return serializer.save()


class CreateJobOrderComment(generics.CreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Comment.objects.all()

    def perform_create(self, serializer):
        user = self.request.user
        job_order_id = self.kwargs.get("id")
        ticket_number = self.kwargs.get("ticket_number")
        job_order = get_object_or_404(JobOrderGeneral, id=job_order_id)
        JobOrderCommentEmail(
            job_order.ticket_number,
            job_order,
            job_order.client_email,
            job_order.staff_email,
        ).send()
        serializer.save(user=user, job_order=job_order)
