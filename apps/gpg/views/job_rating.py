from django.contrib.auth import get_user_model

from rest_framework import viewsets, permissions, generics
from rest_framework.generics import get_object_or_404

from apps.authentication.models import Client
from apps.gpg.models import (
    JobOrderGeneralRating,
    JobOrderCategoryRating,
    JobOrderGeneral,
    JobOrderCategory,
)
from apps.gpg.serializers import (
    JobOrderCategoryRatingSerializer,
    JobOrderGeneralRatingSerializer,
)

User = get_user_model()


__all__ = ("JobOrderGeneralRatingView", "JobOrderCategoryRatingView")


class JobOrderGeneralRatingView(generics.CreateAPIView):
    serializer_class = JobOrderGeneralRatingSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = JobOrderGeneralRating.objects.select_related("client", "job_order").all()

    def perform_create(self, serializer):
        user = self.request.user
        client = Client.objects.get(user=user)
        job_order_id = self.kwargs.get("id")
        job_order = get_object_or_404(JobOrderGeneral, id=job_order_id)
        serializer.save(client=client, job_order=job_order)


class JobOrderCategoryRatingView(generics.CreateAPIView):
    serializer_class = JobOrderCategoryRatingSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = JobOrderCategoryRating.objects.select_related(
        "client", "job_order"
    ).all()

    def perform_create(self, serializer):
        user = self.request.user
        client = Client.objects.get(user=user)
        job_order_id = self.kwargs.get("job_order_id")
        job_order = get_object_or_404(JobOrderCategory, id=job_order_id)
        serializer.save(client=client, job_order=job_order)
