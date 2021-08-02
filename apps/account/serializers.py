from rest_framework import serializers

from apps.authentication.models import Client, Staff
from apps.account.models import LoginCredential, AccountFile


class LoginCredentialSerializer(serializers.ModelSerializer):
    client = serializers.SlugRelatedField(
        slug_field="client_code",
        queryset=Client.objects.all(),
        required=False,
        allow_null=True,
    )

    class Meta:
        model = LoginCredential
        fields = (
            "id",
            "client",
            "category",
            "url",
            "username",
            "password",
            "notes",
            "staff",
        )


class AccountFileSerializer(serializers.ModelSerializer):
    client = serializers.PrimaryKeyRelatedField(
        queryset=Client.objects.all(), required=False, allow_null=True
    )
    client_code = serializers.SerializerMethodField()

    class Meta:
        model = AccountFile
        fields = (
            "id",
            "client",
            "client_code",
            "file_name",
            "url",
            "file_description",
            "staff",
        )

    def get_client_code(self, instance):
        return f"{instance.client.client_code}"
