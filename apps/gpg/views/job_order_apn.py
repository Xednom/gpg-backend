from django.conf import settings

from post_office.models import EmailTemplate
from post_office import mail

from django.contrib.auth import get_user_model
from django.core.mail import send_mail

from django_filters import CharFilter
from django_filters import rest_framework as dfilters

from rest_framework import viewsets, permissions, generics, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

from notifications.signals import notify

from apps.authentication.models import Staff, Client, User
from apps.gpg.models import (
    JobOrderCategory,
    CommentByApn,
    PropertyDetail,
    PropertyPrice,
    CategoryType,
    Deadline,
    State,
    County,
    PropertyDetailFile,
    JobOrderCategoryAnalytics,
)
from apps.gpg.serializers import (
    PropertyDetailSerializer,
    PropertyPriceSerializer,
    CategoryTypeSerializer,
    JobOrderCategorySerializer,
    CommentByApnSerializer,
    ApnCommentSerializer,
    DeadlineSerializer,
    StateSerializer,
    CountySerializer,
    PropertyDetailFileSerializer,
    JobOrderApnAnalyticsSerializer,
)

User = get_user_model()


__all__ = (
    "PropertyDetailsViewSet",
    "JobOrderByCategoryViewSet",
    "CreateJobOrderByApnComment",
    "ApnCategoryViewSet",
    "PropertyPriceStatusViewSet",
    "DeadlineViewSet",
    "StateViewSet",
    "CountyViewSet",
    "PropertyDetailFileViewSet",
    "JobOrderApnAnalyticsViewSet",
)


class PropertyDetailsViewSet(viewsets.ModelViewSet):
    serializer_class = PropertyDetailSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = "ticket_number"
    filter_backends = [filters.SearchFilter]
    search_fields = ["property_price_statuses__price_status"]

    def get_queryset(self):
        current_user = self.request.user
        user = User.objects.filter(username=current_user)

        if current_user:
            queryset = PropertyDetail.objects.select_related("client").filter(
                client__user__in=user
            ) or PropertyDetail.objects.select_related("client").filter(
                staff__user__in=user
            )
            return queryset
        elif current_user.is_superuser:
            queryset = PropertyDetail.objects.select_related("client").all()
            return queryset

    def perform_update(self, serializer):
        instance = self.get_object()
        ticket_number = instance.ticket_number
        client_email = instance.client_email
        staff_email = instance.staff_email
        staff_emails = staff_email.split()
        property_detail = serializer.validated_data
        # Email notification will only send if two email are present
        if client_email and staff_email:
            email = client_email + " " + staff_email
            emails = email.split()
            mail.send(
                "postmaster@landmaster.us",
                bcc=emails,
                template="property_detail_update",
                context={"property_detail": property_detail},
            )
        return serializer.save()


class PropertyPriceStatusViewSet(viewsets.ModelViewSet):
    serializer_class = PropertyPriceSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ["property_detail__id"]
    queryset = PropertyPrice.objects.all()


class PropertyDetailFileViewSet(viewsets.ModelViewSet):
    serializer_class = PropertyDetailFileSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ["property_detail__id"]
    queryset = PropertyDetailFile.objects.all()


class JobOrderByCategoryViewSet(viewsets.ModelViewSet):
    serializer_class = JobOrderCategorySerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = "ticket_number"

    def get_queryset(self):
        current_user = self.request.user.id
        user = User.objects.filter(id=current_user)

        if current_user:
            queryset = JobOrderCategory.objects.select_related(
                "client", "deadline", "property_detail"
            ).prefetch_related("staff").filter(
                client__user__in=user
            ) or JobOrderCategory.objects.select_related(
                "client", "deadline", "property_detail"
            ).prefetch_related(
                "staff"
            ).filter(
                staff__user__in=user
            ).exclude(
                status="complete"
            ).exclude(
                status="closed"
            )
            return queryset
        elif current_user.is_superuser:
            queryset = (
                JobOrderCategory.objects.select_related(
                    "client", "deadline", "property_detail"
                )
                .prefetch_related("staff")
                .all()
            )
            return queryset

    def perform_update(self, serializer):
        instance = self.get_object()
        user = self.request.user
        user = User.objects.filter(username=user).first()
        ticket_number = instance.ticket_number
        client_email = instance.client_email
        staff_email = instance.staff_email
        staff_emails = staff_email.split()
        client = [instance.client.user]
        staff = [staff.user for staff in instance.staff.all()]
        recipient = client + staff
        job_order_category = serializer.validated_data
        if client_email and staff_email:
            emails = client_email + " " + staff_email
            emails = emails.split()
            mail.send(
                "postmaster@landmaster.us",
                bcc=emails,
                template="job_order_category_update",
                context={"job_order_category": job_order_category},
            )
        notify.send(actor=id, sender=user, recipient=recipient, verb="updated", target=instance, action_object=instance)
        return serializer.save()


class ApnCategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategoryTypeSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = CategoryType.objects.all()


class DeadlineViewSet(viewsets.ModelViewSet):
    serializer_class = DeadlineSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Deadline.objects.all()


class CreateJobOrderByApnComment(generics.CreateAPIView):
    serializer_class = ApnCommentSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = CommentByApn.objects.select_related("job_order_category", "user").all()

    def perform_create(self, serializer):
        user = self.request.user
        job_order_id = self.kwargs.get("id")
        job_order = get_object_or_404(JobOrderCategory, id=job_order_id)
        if job_order.client_email and job_order.staff_email:
            staff_email = job_order.staff_email
            emails = job_order.client_email + " " + staff_email
            emails = emails.split()
            mail.send(
                "postmaster@landmaster.us",
                bcc=emails,
                template="job_order_category_comment",
                context={"job_order": job_order},
            )
        serializer.save(user=user, job_order_category=job_order)


class StateViewSet(viewsets.ModelViewSet):
    serializer_class = StateSerializer
    pagination_class = None
    permission_classes = [permissions.IsAuthenticated]
    queryset = State.objects.all()


class CountyViewSet(viewsets.ModelViewSet):
    serializer_class = CountySerializer
    pagination_class = None
    permission_classes = [permissions.IsAuthenticated]
    queryset = County.objects.select_related("state").all()
    filter_backends = [filters.SearchFilter]
    search_fields = ["state__name"]


class JobOrderApnAnalyticsFilter(dfilters.FilterSet):
    month = CharFilter(field_name="month", lookup_expr="icontains")
    month_year = CharFilter(field_name="month_year", lookup_expr="icontains")

    class Meta:
        model = JobOrderCategoryAnalytics
        fields = ("month", "month_year")


class JobOrderApnAnalyticsViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = JobOrderApnAnalyticsSerializer
    permission_clases = [permissions.IsAuthenticated]
    filter_backends = [dfilters.DjangoFilterBackend]
    filter_class = JobOrderApnAnalyticsFilter

    def get_queryset(self):
        current_user = self.request.user.id
        user = User.objects.filter(id=current_user)
        if current_user:
            queryset = JobOrderCategoryAnalytics.objects.select_related(
                "client"
            ).filter(client__user__in=user)
            return queryset
