from rest_framework import serializers

from apps.resolution.models import Resolution, Category
from apps.authentication.models import Staff


__all__ = ("ResolutionSerializer",)


class ResolutionSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        slug_field="name", queryset=Category.objects.all()
    )
    assigned_to = serializers.SlugRelatedField(
        slug_field="user", queryset=Staff.objects.all()
    )

    class Meta:
        model = Resolution
        fields = (
            "id",
            "date_submitted",
            "category",
            "description",
            "assigned_to",
            "resolution_provided_by_management",
            "status",
            "additional_notes",
        )
