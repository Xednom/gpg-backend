from django.contrib.auth import get_user_model
from rest_framework import viewsets, permissions, generics

from apps.authentication.models import Staff, Client, User
from apps.gpg.models import (
    JobOrderCategory,
    CommentByApn,
    PropertyDetail,
    CategoryType,
)
from apps.gpg.serializers import (
    PropertyDetailSerializer,
    CategoryTypeSerializer,
    JobOrderCategorySerializer,
    CommentByApnSerializer
)

User = get_user_model()


__all__ = ("PropertyDetailsViewSet", "JobOrderByCategoryViewSet")


class PropertyDetailsViewSet(viewsets.ModelViewSet):
    serializer_class = PropertyDetailSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = "ticket_number"

    def get_queryset(self):
        job_order = PropertyDetail.objects.all()
        current_user = self.request.user
        user = User.objects.filter(username=current_user)

        if current_user:
            queryset = job_order.filter(client__user__in=user) or job_order.filter(staff__user__in=user)
            return queryset
        elif current_user.is_superuser:
            queryset = PropertyDetail.objects.all()
            return queryset


class JobOrderByCategoryViewSet(viewsets.ModelViewSet):
    serializer_class = JobOrderCategorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        job_order = JobOrderCategory.objects.all()
        current_user = self.request.user
        user = User.objects.filter(username=current_user)

        if current_user:
            queryset = job_order.filter(client__user__in=user) or job_order.filter(va_assigned__user__in=user)
            return queryset
        elif current_user.is_superuser:
            queryset = JobOrderCategory.objects.all()
            return queryset


class CreateJobOrderByApnComment(generics.CreateAPIView):
    serializer_class = CommentByApnSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = CommentByApn.objects.all()

    def perform_create(self, serializer):
        user = self.request.user
        job_order_id = self.kwargs.get("id")
        job_order = get_object_or_404(JobOrderCategory, id=job_order_id)

        serializer.save(user=user, job_order=job_order)