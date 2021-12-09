from rest_framework import serializers

from apps.resolution.models import Resolution, Category
from apps.authentication.models import Staff, Client


__all__ = ("ResolutionSerializer", "CategorySerializer")


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name")


class ResolutionSerializer(serializers.ModelSerializer):
    client = serializers.PrimaryKeyRelatedField(
        queryset=Client.objects.all(), required=False, allow_null=True
    )
    category = serializers.SlugRelatedField(
        slug_field="name",
        queryset=Category.objects.all(),
        required=False,
        allow_null=True,
    )
    assigned_to = serializers.SlugRelatedField(
        slug_field="user", queryset=Staff.objects.all(), required=False, allow_null=True
    )
    client_name = serializers.SerializerMethodField()

    class Meta:
        model = Resolution
        fields = (
            "id",
            "date_submitted",
            "category",
            "description",
            "assigned_to",
            "client",
            "client_name",
            "resolution_provided_by_management",
            "status",
            "additional_notes",
        )
    
    def get_client_name(self, obj):
        return obj.client.user.get_full_name() if obj.client else None
