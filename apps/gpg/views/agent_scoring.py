from django.contrib.auth import get_user_model

from rest_framework import viewsets, permissions

from apps.gpg.models import JobOrderGeneralAgentScoring, JobOrderCategoryAgentScoring
from apps.gpg.serializers import (
    JobOrderGeneralAgentScoringSerializer,
    JobOrderCategoryAgentScoringSerializer,
)

User = get_user_model()


__all__ = ("JobOrderGeneralAgentScoringViewSet", "JobOrderCategoryAgentScoringViewSet")


class JobOrderGeneralAgentScoringViewSet(viewsets.ModelViewSet):
    queryset = JobOrderGeneralAgentScoring.objects.all()
    serializer_class = JobOrderGeneralAgentScoringSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        current_user = self.request.user
        user = User.objects.filter(username=current_user)
        queryset = JobOrderGeneralAgentScoring.objects.select_related(
            "staff", "client", "job_order_general"
        ).filter(
            client__user__in=user
        ) or JobOrderGeneralAgentScoring.objects.select_related(
            "staff", "client", "job_order_generalu"
        ).filter(
            staff__user__in=user
        )
        return queryset


class JobOrderCategoryAgentScoringViewSet(viewsets.ModelViewSet):
    queryset = JobOrderCategoryAgentScoring.objects.all()
    serializer_class = JobOrderCategoryAgentScoringSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        current_user = self.request.user
        user = User.objects.filter(username=current_user)
        queryset = JobOrderGeneralAgentScoring.objects.select_related(
            "staff", "client", "job_order_general"
        ).filter(
            client__user__in=user
        ) or JobOrderGeneralAgentScoring.objects.select_related(
            "staff", "client", "job_order_generalu"
        ).filter(
            staff__user__in=user
        )
        return queryset
