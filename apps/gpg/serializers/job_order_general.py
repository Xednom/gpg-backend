from rest_framework import serializers

from apps.gpg.models import JobOrderGeneral


class JobOrderGeneralSerializer(serializers.ModelSerializer):
    client = serializers.CharField(source="client.client_name")
    va_assigned = serializers.CharField(source="va_assigned.staff_name")
    client_code = serializers.SerializerMethodField()
    class Meta:
        model = JobOrderGeneral
        fields = (
            "id",
            "ticket_number",
            "client",
            "client_code",
            "va_assigned",
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
        return instance.client.client_code
