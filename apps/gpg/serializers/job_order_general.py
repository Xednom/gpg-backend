from rest_framework import serializers

from apps.gpg.models import JobOrderGeneral


class JobOrderGeneralSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobOrderGeneral
        fields = (
            "client",
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