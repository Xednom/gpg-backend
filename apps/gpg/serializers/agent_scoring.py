from rest_framework import serializers

from apps.authentication.models import Client, Staff
from apps.gpg.models import (
    JobOrderGeneral,
    JobOrderCategory,
    JobOrderGeneralAgentScoring,
    JobOrderCategoryAgentScoring,
)


__all__ = (
    "JobOrderGeneralAgentScoringSerializer",
    "JobOrderCategoryAgentScoringSerializer",
)


class JobOrderGeneralAgentScoringSerializer(serializers.ModelSerializer):
    staff = serializers.SlugRelatedField(
        slug_field="staff_id", queryset=Staff.objects.all()
    )
    client = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all())
    job_order_general = serializers.SlugRelatedField(
        slug_field="ticket_number", queryset=JobOrderGeneral.objects.all()
    )

    class Meta:
        model = JobOrderGeneralAgentScoring
        fields = (
            "id",
            "staff",
            "client",
            "job_order_general",
            "accuracy",
            "speed",
            "quality_of_work",
            "delivered_on_time",
            "delivery_note",
            "job_completed",
            "job_completed_note",
            "satisfied",
        )


class JobOrderCategoryAgentScoringSerializer(serializers.ModelSerializer):
    staff = serializers.SlugRelatedField(
        slug_field="staff_id", queryset=Staff.objects.all()
    )
    client = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all())
    job_order_category = serializers.SlugRelatedField(
        slug_field="ticket_number", queryset=JobOrderCategory.objects.all()
    )

    class Meta:
        model = JobOrderCategoryAgentScoring
        fields = (
            "id",
            "staff",
            "client",
            "job_order_category",
            "accuracy",
            "speed",
            "quality_of_work",
            "delivered_on_time",
            "delivery_note",
            "job_completed",
            "job_completed_note",
            "satisfied",
        )
