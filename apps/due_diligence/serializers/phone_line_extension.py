from rest_framework import serializers

from apps.due_diligence.models import PhoneLineExtension


__all__ = ("PhoneLineExtSerializer",)


class PhoneLineExtSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneLineExtension
        fields = ("id", "user_id", "code_name")
