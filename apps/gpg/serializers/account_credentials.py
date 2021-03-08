from rest_framework import serializers

from apps.gpg.models import AccountCredential


class AccountCredentialSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountCredential
        fields = (
            "client",
            "category",
            "url",
            "username",
            "password",
            "notes",
            "granted_access_to",
            "access_granted"
        )