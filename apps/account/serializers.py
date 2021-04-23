from rest_framework import serializers

from apps.authentication.models import Client, Staff
from apps.account.models import LoginCredential


class LoginCredentialSerializer(serializers.ModelSerializer):
    client = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all(), required=False, allow_null=True)

    class Meta:
        model = LoginCredential
        fields = (
            "client",
            "category",
            "username",
            "password",
            "notes",
            "staff"
        )