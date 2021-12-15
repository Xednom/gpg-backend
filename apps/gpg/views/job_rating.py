from django.contrib.auth import get_user_model

from rest_framework import viewsets, permissions, generics
from rest_framework.generics import get_object_or_404

from apps.authentication.models import Client
from apps.gpg.models import JobOrderGeneralRating, JobOrderCategoryRating
from apps.gpg.serializers import (
    JobOrderCategoryRatingSerializer,
    JobOrderGeneralRatingSerializer,
)

User = get_user_model()


__all__ = ("JobOrderGeneralRatingView", "JobOrderCategoryRatingView")


class JobOrderGeneralRatingView(generics.ListCreateAPIView):
    serializer_class = JobOrderGeneralRatingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        job_order_id = self.kwargs.get("job_order_id")
        job_order = get_object_or_404(JobOrderGeneralRating, id=job_order_id)
        queryset = JobOrderGeneralRating.objects.select_related(
            "job_order", "client"
        ).filter(client=user, job_order=job_order)
        return queryset

    def perform_create(self, serializer):
        user = self.request.user
        job_order_id = self.kwargs.get("job_order_id")
        job_order = get_object_or_404(JobOrderGeneralRating, id=job_order_id)
        serializer.save(client=user, job_order=job_order)


class JobOrderCategoryRatingView(generics.ListCreateAPIView):
    serializer_class = JobOrderCategoryRatingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        job_order_id = self.kwargs.get("job_order_id")
        job_order = get_object_or_404(JobOrderGeneralRating, id=job_order_id)
        queryset = JobOrderGeneralRating.objects.select_related(
            "job_order", "client"
        ).filter(client=user, job_order=job_order)
        return queryset

    def perform_create(self, serializer):
        user = self.request.user
        job_order_id = self.kwargs.get("job_order_id")
        job_order = get_object_or_404(JobOrderGeneralRating, id=job_order_id)
        serializer.save(client=user, job_order=job_order)
