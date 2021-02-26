from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer

from django.contrib.auth import get_user_model
from .models import Client, Staff, InternalFiles, InternalFilesStaff

from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer
from djoser.serializers import UserSerializer as BaseUserListSerializer


class UserRegistrationSerializer(BaseUserRegistrationSerializer):
    class Meta(BaseUserRegistrationSerializer.Meta):
        fields = (
            "username",
            "password",
            "first_name",
            "last_name",
            "email",
            "phone",
            "designation_category",
            "company_category",
        )


class UserListSerializer(BaseUserListSerializer):
    class Meta(BaseUserListSerializer.Meta):
        fields = BaseUserListSerializer.Meta.fields + (
            "email",
            "phone",
            "designation_category",
            "company_category",
        )


class ClientInternalFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = InternalFiles
        fields = ("id", "client", "file_name", "url", "description")

    def update(self, instance, validated_data):
        instance.file_name = validated_data.get("file_name", instance.file_name)
        instance.url = validated_data.get("url", instance.url)
        instance.description = validated_data.get("description", instance.description)
        instance.save()
        return instance


class ClientSerializer(WritableNestedModelSerializer):
    client_files = ClientInternalFileSerializer(many=True, allow_null=True, required=False)
    class Meta:
        model = Client
        fields = (
            "id",
            "client_code",
            "affiliate_partner_code",
            "affiliate_partner_name",
            "pin",
            "lead_information",
            "customer_id",
            "client_files",
        )
        # lookup_field = "user"


class StaffSerializer(serializers.ModelSerializer):
    staff_files = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=InternalFilesStaff.objects.all(),
        required=False,
    )

    class Meta:
        model = Staff
        fields = (
            "date_of_birth",
            "blood_type",
            "position",
            "company_id",
            "staff_id",
            "phone_number",
            "company_email",
            "start_date_hired",
            "date_hired_in_contract",
            "base_pay",
            "hourly_rate",
            "status",
            "category",
            "residential_address",
            "tin_number",
            "sss_number",
            "pag_ibig_number",
            "phil_health_number",
            "emergency_contact_full_name",
            "relationship",
            "emergency_contact_number",
            "mothers_full_name",
            "mothers_maiden_name",
            "fathers_full_name",
            "bank_name",
            "bank_account_name",
            "bank_type",
            "bank_account_number",
            "staff_files",
        )


class CurrentUserSerializer(BaseUserListSerializer, WritableNestedModelSerializer):
    client = ClientSerializer()
    staff = StaffSerializer(allow_null=True, required=False)

    class Meta(BaseUserListSerializer.Meta):
        fields = BaseUserListSerializer.Meta.fields + (
            "phone",
            "first_name",
            "last_name",
            "designation_category",
            "company_category",
            "client",
            "staff"
        )

    def update(self, instance, validated_data):
        client_data = validated_data.pop("client")
        # client_data_files = validated_data.pop("client.client_files", [])
        client = instance.client
        # client_files = instance.client.client_files

        # user account info
        instance.first_name = validated_data.get("first_name", instance.first_name)
        instance.last_name = validated_data.get("last_name", instance.last_name)
        instance.phone = validated_data.get("phone", instance.phone)
        instance.email = validated_data.get("email", instance.email)
        instance.designation_category = validated_data.get(
            "designation_category", instance.designation_category
        )
        instance.company_category = validated_data.get(
            "company_category", instance.company_category
        )
        instance.save()

        # client info
        client.client_code = client_data.get("client_code", client.client_code)
        client.affiliate_partner_code = client_data.get(
            "affiliate_partner_code", client.affiliate_partner_code
        )
        client.affiliate_partner_name = client_data.get(
            "affiliate_partner_name", client.affiliate_partner_name
        )
        client.pin = client_data.get("pin", client.pin)
        client.lead_information = client_data.get(
            "lead_information", client.lead_information
        )
        client.customer_id = client_data.get("customer_id", client.customer_id)
        # client.client_files = client_data.get("client_files", client.client_files)
        return instance
