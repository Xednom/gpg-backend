from django.utils import timezone
from django.contrib.auth import get_user_model

from notifications.models import Notification

from rest_framework import serializers

from apps.authentication.models import Client, Staff
from apps.authentication.serializers import ClientCodeSerializer, StaffCodeSerializer
from apps.gpg.models import JobOrderGeneral, JobOrderCategory
from apps.gpg.serializers import JobOrderGeneralNotifSerializer, JobOrderCategoryNotifSerializer

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    user_clients = ClientCodeSerializer(read_only=True)
    staff = StaffCodeSerializer(read_only=True)
    class Meta:
        model = get_user_model()
        fields = (
            "id",
            "username",
            "user_clients",
            "staff",
        )


class GenericNotificationRelatedField(serializers.RelatedField):
    User = get_user_model()

    def to_representation(self, value):
        if isinstance(value, JobOrderGeneral):
            serializer = JobOrderGeneralNotifSerializer(value)
            return serializer.data
        elif isinstance(value, JobOrderCategory):
            serializer = JobOrderCategoryNotifSerializer(value)
            return serializer.data
        elif isinstance(value, User):
            serializer = UserSerializer(value)

            return serializer.data


class NotificationSerializer(serializers.ModelSerializer):
    recipient = UserSerializer(read_only=True)
    unread = serializers.BooleanField(required=False, allow_null=True)
    target = GenericNotificationRelatedField(read_only=True)
    verb = serializers.CharField(required=False, allow_null=True)
    actor = UserSerializer(read_only=True)
    actor_object_id = serializers.IntegerField(required=False, allow_null=True)
    actor_content_type = serializers.CharField(required=False, allow_null=True)
    was_published = serializers.SerializerMethodField()
    staff = serializers.SerializerMethodField()
    client = serializers.SerializerMethodField()

    class Meta:
        model = Notification
        fields = "__all__"

    def get_staff(self, instance):
        staff = [staff.staff_id for staff in Staff.objects.filter(user__username=instance.actor.username)]
        return "".join(staff)
    
    def get_client(self, instance):
        client = [client.client_code for client in Client.objects.filter(user__username=instance.actor.username)]
        return "".join(client)

    def get_was_published(self, instance):
        now = timezone.now()
        published = now - instance.timestamp
        if published.days == 0:
            return "today"
        return published.days
