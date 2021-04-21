from django.conf import settings

from post_office.models import EmailTemplate
from post_office import mail
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from rest_framework import viewsets, permissions, generics, filters, status
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

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
    PropertyDetailFile
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
    PropertyDetailFileSerializer
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
    "PropertyDetailFileViewSet"
)


class PropertyDetailsViewSet(viewsets.ModelViewSet):
    serializer_class = PropertyDetailSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = "apn"
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
            mail.send(
                [client_email],
                cc=staff_emails,
                template="property_detail_update",
                context={
                    "property_detail": property_detail
                 },
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
            ).filter(client__user__in=user) or JobOrderCategory.objects.select_related(
                "client", "deadline", "property_detail"
            ).filter(
                staff__user__in=user
            )
            return queryset
        elif current_user.is_superuser:
            queryset = JobOrderCategory.objects.select_related(
                "client", "deadline", "property_detail"
            ).all()
            return queryset

    def perform_update(self, serializer):
        instance = self.get_object()
        ticket_number = instance.ticket_number
        client_email = instance.client_email
        staff_email = instance.staff_email
        staff_emails = staff_email.split()
        job_order_category = serializer.validated_data
        if client_email and staff_email:
            mail.send(
                [client_email],
                cc=staff_emails,
                template="job_order_category_update",
                context={
                    "job_order_category": job_order_category
                 },
            )
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
            mail.send(
                [job_order.staff_email, job_order.client_email],
                template="job_order_category_comment",
                context={
                    "job_order": job_order
                 },
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
