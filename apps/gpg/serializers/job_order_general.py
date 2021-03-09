from rest_framework import serializers

from apps.authentication.models import Staff, Client
from apps.gpg.models import JobOrderGeneral


class JobOrderGeneralSerializer(serializers.ModelSerializer):
    # va_assigned = serializers.SlugRelatedField(slug_field="staff_name", queryset=Staff.objects.all(), allow_null=True, required=False)
    # client = serializers.SlugRelatedField(slug_field="client_name", queryset=Client.objects.all(), allow_null=True, required=False)
    client_code = serializers.SerializerMethodField()
    client_name = serializers.SerializerMethodField()
    staff_name = serializers.SerializerMethodField()
    class Meta:
        model = JobOrderGeneral
        fields = (
            "id",
            "ticket_number",
            "client",
            "client_name",
            "client_code",
            "va_assigned",
            "staff_name",
            "request_date",
            "due_date",
            "job_title",
            "job_description",
            "client_notes",
            "va_notes",
            "status",
            "date_completed",
            "total_time_consumed"
        )
    
    def get_client_code(self, instance):
        if instance.client is None:
            return "Management on process"
        else:
            return instance.client.client_code
    
    def get_staff_name(self, instance):
        if instance.va_assigned is None:
            return "processing a VA"
        else:
            return instance.va_assigned.staff_name
    
    def get_client_name(self, instance):
        if instance.client is None:
            return "Management on process"
        else:
            return instance.client.client_name
