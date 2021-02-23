from rest_framework import serializers

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
            "company_category"
        )


class UserListSerializer(BaseUserListSerializer):
    class Meta(BaseUserListSerializer.Meta):
        fields = BaseUserListSerializer.Meta.fields + (
            "email",
            "phone",
            "designation_category",
            "company_category"
        )


class ClientSerializer(serializers.ModelSerializer):
    client_files = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=InternalFiles.objects.all(),
        required=False
    )
    class Meta:
        model = Client
        fields = (
            "user",
            "client_code",
            "affiliate_partner_code",
            "affiliate_partner_name",
            "pin",
            "lead_information",
            "customer_id",
            "client_files"
        )


class StaffSerializer(serializers.ModelSerializer):
    staff_files = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=InternalFilesStaff.objects.all(),
        required=False,
    )

    class Meta:
        model = Staff
        fields = (
            "user",
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
            "staff_files"
        )