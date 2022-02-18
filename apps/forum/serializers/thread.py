from django.contrib.auth import get_user_model

from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer

from apps.authentication.models import Client, Staff
from apps.forum.models import Thread, Comment, Reply

User = get_user_model()


__all__ = ("ThreadSerializer", "CommentSerializer", "ReplySerializer")


class StaffCarbonCopySerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = ("staff_id",)


class ClientCarbonCopySerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ("client_code",)


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), required=False, allow_null=True
    )
    thread = serializers.PrimaryKeyRelatedField(
        queryset=Thread.objects.all(), required=False, allow_null=True
    )
    user_type = serializers.SerializerMethodField()
    commenter = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = (
            "id",
            "thread",
            "author",
            "comment",
            "commenter",
            "created_at",
            "user_type",
        )

    def get_user_type(self, instance):
        staff_user = "staff"
        client_user = "client"
        if instance.author.designation_category == "staff":
            return staff_user
        elif instance.author.designation_category != "staff":
            return client_user

    def get_commenter(self, instance):
        get_staff_code = Staff.objects.select_related("user").filter(
            user=instance.author
        )
        get_client_code = Client.objects.select_related("user").filter(
            user=instance.author
        )

        if instance.author.designation_category == "staff":
            staff_code = [staff.staff_id for staff in get_staff_code]
            staff_code = "".join(staff_code)
            return staff_code
        elif instance.author.designation_category != "staff":
            client_code = [client.client_code for client in get_client_code]
            client_code = "".join(client_code)
            return client_code


class ThreadSerializer(WritableNestedModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    thread_comments = CommentSerializer(many=True, required=False, allow_null=True)
    author_username = serializers.SerializerMethodField()

    class Meta:
        model = Thread
        fields = (
            "id",
            "title",
            "content",
            "author",
            "staff_carbon_copy",
            "client_carbon_copy",
            "is_active",
            "thread_comments",
            "author_username",
        )

    def get_author_username(self, instance):
        get_staff_code = Staff.objects.select_related("user").filter(
            user=instance.author
        )
        get_client_code = Client.objects.select_related("user").filter(
            user=instance.author
        )

        if instance.author.designation_category == "staff":
            staff_code = [staff.staff_id for staff in get_staff_code]
            staff_code = "".join(staff_code)
            return staff_code
        elif instance.author.designation_category != "staff":
            client_code = [client.client_code for client in get_client_code]
            client_code = "".join(client_code)
            return client_code


class ReplySerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    comment = serializers.PrimaryKeyRelatedField(queryset=Comment.objects.all())

    class Meta:
        model = Reply
        fields = (
            "id",
            "comment",
            "author",
            "content",
        )
