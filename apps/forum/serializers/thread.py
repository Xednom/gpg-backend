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
    author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    thread = serializers.PrimaryKeyRelatedField(queryset=Thread.objects.all())

    class Meta:
        model = Comment
        fields = (
            "id",
            "thread",
            "author",
            "comment",
        )


class ThreadSerializer(WritableNestedModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    thread_comments = CommentSerializer(many=True, required=False, allow_null=True)
    author_name = serializers.SerializerMethodField()

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
            "author_name",
        )

    def get_author_name(self, instance):
        return f"{instance.author.first_name} {instance.author.last_name}"


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
