from django.conf import settings

from post_office.models import EmailTemplate
from post_office import mail

from django_filters import CharFilter
from django_filters import rest_framework as dfilters

from django.contrib.auth import get_user_model
from rest_framework import viewsets, permissions, generics
from rest_framework.generics import get_object_or_404

from apps.authentication.models import Client, Staff
from apps.gpg.models import JobOrderGeneral, Comment, JobOrderGeneralAnalytics
from apps.gpg.serializers import JobOrderGeneralSerializer, CommentSerializer, JobOrderGeneralAnalyticsSerializer

from notifications.signals import notify

User = get_user_model()


class JobOrderGeneralViewSet(viewsets.ModelViewSet):
    serializer_class = JobOrderGeneralSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = "ticket_number"

    def get_queryset(self):
        current_user = self.request.user
        clients = User.objects.filter(username=current_user)
        staffs = User.objects.filter(username=current_user)
        client = clients.all()
        staff = staffs.all()

        if current_user:
            queryset = JobOrderGeneral.objects.select_related(
                "client"
            ).prefetch_related("va_assigned").filter(
                client__user__in=client
            ) or JobOrderGeneral.objects.select_related(
                "client"
            ).prefetch_related(
                "va_assigned"
            ).filter(
                va_assigned__user__in=staff
            ).exclude(
                status="complete"
            ).exclude(
                status="closed"
            )
            return queryset
        else:
            queryset = JobOrderGeneral.objects.all()
            return queryset

    def perform_create(self, serializer):
        user = self.request.user
        user = User.objects.filter(id=self.request.user.id)
        serializer.save(updated_by=user)

    def perform_update(self, serializer):
        instance = self.get_object()
        user = self.request.user
        user = User.objects.filter(username=user).first()
        id = self.kwargs.get("va_assigned.staff_id") or self.kwargs.get("client.customer_id")
        client_email = instance.client_email
        staff_email = instance.staff_email
        job_order = serializer.validated_data
        client = [instance.client.user]
        staff = [staff.user for staff in instance.va_assigned.all()]
        recipient = client + staff
        serializer.save(updated_by=user)
        if client_email and staff_email:
            emails = client_email + " " + staff_email
            emails = emails.split()
            mail.send(
                "postmaster@landmaster.us",
                bcc=emails,
                template="job_order_general_update",
                context={"job_order": job_order},
            )
            notify.send(actor=id, sender=user, recipient=recipient, verb="updated", target=instance, action_object=instance)


class CreateJobOrderComment(generics.CreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Comment.objects.select_related("job_order", "user").all()

    def perform_create(self, serializer):
        user = self.request.user
        job_order_id = self.kwargs.get("id")
        ticket_number = self.kwargs.get("ticket_number")
        job_order = get_object_or_404(JobOrderGeneral, id=job_order_id)
        if job_order.client_email and job_order.staff_email:
            emails = job_order.client_email + " " + job_order.staff_email
            emails = emails.split()
            mail.send(
                "postmaster@landmaster.us",
                bcc=emails,
                template="job_order_comment_update",
                context={"job_order": job_order},
            )
        serializer.save(user=user, job_order=job_order)


class JobOrderApnAnalyticsFilter(dfilters.FilterSet):
    month = CharFilter(field_name="month", lookup_expr="icontains")
    month_year = CharFilter(field_name="month_year", lookup_expr="icontains")

    class Meta:
        model = JobOrderGeneralAnalytics
        fields = ("month", "month_year")


class JobOrderGeneralAnalyticsViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = JobOrderGeneralAnalyticsSerializer
    permission_clases = [permissions.IsAuthenticated]
    filter_backends = [dfilters.DjangoFilterBackend]
    filter_class = JobOrderApnAnalyticsFilter

    def get_queryset(self):
        current_user = self.request.user.id
        user = User.objects.filter(id=current_user)
        if current_user:
            queryset = JobOrderGeneralAnalytics.objects.select_related(
                "client"
            ).filter(client__user__in=user)
            return queryset