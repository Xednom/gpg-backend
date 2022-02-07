from django.contrib.auth import get_user_model

from notifications.models import Notification

from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = (
            "id",
            "username",
        )


class GenericNotificationRelatedField(serializers.RelatedField):
    User = get_user_model()

    def to_representation(self, value):
        if isinstance(value, User):
            serializer = UserSerializer(value)

        return serializer.data


class NotificationSerializer(serializers.ModelSerializer):
    recipient = UserSerializer(read_only=True)
    unread = serializers.BooleanField(read_only=True)
    target = GenericNotificationRelatedField(read_only=True)
    verb = serializers.CharField()

    class Meta:
        model = Notification
        fields = "__all__"
