from rest_framework import serializers

from apps.gpg.models import (
    JobOrderGeneralRating,
    JobOrderCategoryRating,
    JobOrderGeneral,
    JobOrderCategory,
)
from apps.authentication.models import Client


__all__ = ("JobOrderGeneralRatingSerializer", "JobOrderCategoryRatingSerializer")


class JobOrderGeneralRatingSerializer(serializers.ModelSerializer):
    client = serializers.PrimaryKeyRelatedField(
        queryset=Client.objects.all(), required=False, allow_null=True
    )
    job_order = serializers.PrimaryKeyRelatedField(
        queryset=JobOrderGeneral.objects.all(), required=False, allow_null=True
    )

    class Meta:
        model = JobOrderGeneralRating
        fields = (
            "job_order",
            "rating",
            "comment",
            "client",
        )


class JobOrderCategoryRatingSerializer(serializers.ModelSerializer):
    client = serializers.PrimaryKeyRelatedField(
        queryset=Client.objects.all(), required=False, allow_null=True
    )
    job_order = serializers.PrimaryKeyRelatedField(
        queryset=JobOrderCategory.objects.all(), required=False, allow_null=True
    )

    class Meta:
        model = JobOrderCategoryRating
        fields = (
            "job_order",
            "rating",
            "comment",
            "client",
        )
