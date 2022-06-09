from django.contrib.auth import get_user_model

from rest_framework import serializers

from apps.resolution.models import Resolution, ResolutionComment, Category
from apps.authentication.models import Staff, Client


User = get_user_model()


__all__ = ("ResolutionSerializer", "ResolutionCommentSerializer", "CategorySerializer")


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name")


class ResolutionCommentSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        slug_field="username",
        queryset=User.objects.all(),
        required=False,
        allow_null=True,
    )
    created_at = serializers.DateField(required=False, allow_null=True)
    commenter = serializers.SerializerMethodField()
    user_type = serializers.SerializerMethodField()

    class Meta:
        model = ResolutionComment
        fields = (
            "id",
            "resolution",
            "user",
            "comment",
            "created_at",
            "commenter",
            "user_type",
        )

    def get_user_type(self, instance):
        staff_user = "staff"
        client_user = "client"
        if instance.user:
            if instance.user.designation_category == "staff":
                return staff_user
            elif instance.user.designation_category != "staff":
                return client_user

    def get_commenter(self, instance):
        get_staff_code = Staff.objects.select_related("user").filter(user=instance.user)
        get_client_code = Client.objects.select_related("user").filter(
            user=instance.user
        )

        if instance.user:
            if instance.user.designation_category == "staff":
                staff_code = [staff.staff_id for staff in get_staff_code]
                staff_code = "".join(staff_code)
                return staff_code
            elif instance.user.designation_category != "staff":
                client_code = [client.client_code for client in get_client_code]
                client_code = "".join(client_code)
                return client_code


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
    resolution_comments = ResolutionCommentSerializer(
        many=True, required=False, allow_null=True
    )

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
            "resolution_comments",
        )

    def get_client_name(self, obj):
        return obj.client.user.get_full_name() if obj.client else None
