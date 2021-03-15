from rest_framework import serializers

from apps.authentication.models import Staff, Client
from apps.gpg.models import JobOrderGeneral, Comment


__all__ = ("CommentSerializer", "JobOrderGeneralSerializer")


class CommentSerializer(serializers.ModelSerializer):
    commenter = serializers.SerializerMethodField()
    class Meta:
        model = Comment
        fields = (
            "job_order",
            "user",
            "comment",
            "commenter",
        )
    
    def get_commenter(self, instance):
        if instance.user.designation_category == "staff":
            return "Virtual Assistant"
        else:
            return "Client"


class JobOrderGeneralSerializer(serializers.ModelSerializer):
    job_order_comments = CommentSerializer(many=True, required=False, allow_null=True)
    client_code = serializers.SerializerMethodField()
    client_name = serializers.SerializerMethodField()
    staff_name = serializers.SerializerMethodField()
    status_ = serializers.SerializerMethodField()
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
            "status_",
            "date_completed",
            "total_time_consumed",
            "job_order_comments",
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
    
    def get_status_(self, instance):
        if instance.status == "na": 
            return "N/A"
        elif instance.status == "job_order_request":
            return "Request for job order"
        elif instance.status == "va_processing":
            return "VA Processing"
        elif instance.status == "management_processing":
            return "Management Processing"
        elif instance.status == "verified_job_order":
            return "Verified Job Order"
        elif instance.status == "on_hold":
            return "On Hold"
        elif instance.status == "canceled":
            return "Canceled"
        elif instance.status == "follow_up":
            return "Follow up"
        elif instance.status == "dispute":
            return "Dispute"
        elif instance.status == "complete":
            return "Complete"