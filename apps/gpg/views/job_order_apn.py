from django.conf import settings
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
)
from apps.gpg.serializers import (
    PropertyDetailSerializer,
    PropertyPriceSerializer,
    CategoryTypeSerializer,
    JobOrderCategorySerializer,
    CommentByApnSerializer,
    ApnCommentSerializer,
    DeadlineSerializer,
)

User = get_user_model()


__all__ = (
    "PropertyDetailsViewSet",
    "JobOrderByCategoryViewSet",
    "CreateJobOrderByApnComment",
    "ApnCategoryViewSet",
    "PropertyPriceStatusViewSet",
    "DeadlineViewSet",
)


class PropertyDetailsViewSet(viewsets.ModelViewSet):
    serializer_class = PropertyDetailSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = "ticket_number"
    filter_backends = [filters.SearchFilter]
    search_fields = ["property_price_statuses__price_status"]

    def get_queryset(self):
        job_order = PropertyDetail.objects.all()
        property_price = PropertyPrice.objects.all()
        current_user = self.request.user
        user = User.objects.filter(username=current_user)

        if current_user:
            queryset = job_order.filter(client__user__in=user) or job_order.filter(
                staff__user__in=user
            )
            return queryset
        elif current_user.is_superuser:
            queryset = PropertyDetail.objects.all()
            return queryset

    def perform_update(self, serializer):

        if serializer.is_valid():
            property_status = serializer.validated_data["property_status"]
            ticket_number = serializer.validated_data["ticket_number"]
            client_email = serializer.validated_data["client_email"]
            instance = serializer.save()
            mail_text = "Your ticket with the number {}\n\nStatus has changed {}.\n\nClick below to see the response:\n\n{}".format(
                ticket_number,
                property_status,
                "https://example.com/job-order/property-detail/{ticket_number}",
            )
            try:
                send_mail(
                    subject="Job order per APN",
                    message=mail_text,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=client_email,
                    fail_silently=False,
                )
            except (SMTPRecipientsRefused, SMTPSenderRefused):
                LOGGER.exception("There was a problem submitting the form.")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PropertyPriceStatusViewSet(viewsets.ModelViewSet):
    serializer_class = PropertyPriceSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = PropertyPrice.objects.all()


class JobOrderByCategoryViewSet(viewsets.ModelViewSet):
    serializer_class = JobOrderCategorySerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = "ticket_number"

    def get_queryset(self):
        job_order = JobOrderCategory.objects.all()
        current_user = self.request.user
        user = User.objects.filter(username=current_user)

        if current_user:
            queryset = job_order.filter(client__user__in=user) or job_order.filter(
                staff__user__in=user
            )
            return queryset
        elif current_user.is_superuser:
            queryset = JobOrderCategory.objects.all()
            return queryset


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
    queryset = CommentByApn.objects.all()

    def perform_create(self, serializer):
        user = self.request.user
        job_order_id = self.kwargs.get("id")
        job_order = get_object_or_404(JobOrderCategory, id=job_order_id)

        serializer.save(user=user, job_order_category=job_order)
