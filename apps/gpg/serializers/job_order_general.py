from django.conf import settings

from rest_framework import serializers

from apps.authentication.models import Staff, Client
from apps.gpg.models import JobOrderGeneral, Comment, JobOrderGeneralAnalytics


__all__ = ("CommentSerializer", "JobOrderGeneralSerializer")


class CommentSerializer(serializers.ModelSerializer):
    created_at = serializers.DateField(required=False, allow_null=True)
    commenter = serializers.SerializerMethodField()
    user_type = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = (
            "job_order",
            "user",
            "comment",
            "user_type",
            "commenter",
            "created_at",
        )

    def get_user_type(self, instance):
        staff_user = "staff"
        client_user = "client"
        if instance.user.designation_category == "staff":
            return staff_user
        elif instance.user.designation_category != "staff":
            return client_user

    def get_commenter(self, instance):
        get_staff_code = Staff.objects.select_related("user").filter(user=instance.user)
        get_client_code = Client.objects.select_related("user").filter(
            user=instance.user
        )

        if instance.user.designation_category == "staff":
            staff_code = [staff.staff_id for staff in get_staff_code]
            staff_code = "".join(staff_code)
            return staff_code
        elif instance.user.designation_category != "staff":
            client_code = [client.client_code for client in get_client_code]
            client_code = "".join(client_code)
            return client_code


class JobOrderGeneralSerializer(serializers.ModelSerializer):
    job_order_comments = CommentSerializer(many=True, required=False, allow_null=True)
    client = serializers.SlugRelatedField(
        slug_field="client_code", queryset=Client.objects.all()
    )
    client_code = serializers.SerializerMethodField()
    client_name = serializers.SerializerMethodField()
    status_ = serializers.SerializerMethodField()

    class Meta:
        model = JobOrderGeneral
        fields = (
            "id",
            "created_at",
            "ticket_number",
            "client",
            "client_email",
            "client_name",
            "client_code",
            "va_assigned",
            "staff_email",
            "request_date",
            "due_date",
            "job_title",
            "job_description",
            "client_notes",
            "va_notes",
            "management_notes",
            "status",
            "status_",
            "date_completed",
            "total_time_consumed",
            "url_of_the_completed_jo",
            "job_order_comments",
        )

    def get_client_code(self, instance):
        if instance.client is None:
            return "Management on process"
        else:
            return instance.client.client_code

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
        elif instance.status == "closed":
            return "Closed"
        elif instance.status == "follow_up":
            return "Follow up"
        elif instance.status == "dispute":
            return "Dispute"
        elif instance.status == "complete":
            return "Complete"
        elif instance.status == "under_quality_review":
            return "Under Quality Review"
        elif instance.status == "daily_tasks":
            return "Daily Tasks"
        elif instance.status == "weekly_tasks":
            return "Weekly Tasks"
        elif instance.status == "monthly_tasks":
            return "Monthly Tasks"
        elif instance.status == "redo":
            return "Redo"
        elif instance.status == "pending":
            return "Pending"
        elif instance.status == "request_for_posting":
            return "Request for Posting"
        elif instance.status == "mark_as_sold_request":
            return "Mark as Sold Request"
        elif instance.status == "multiple_task":
            return "Multiple task"
        elif instance.status == "va_assigned_multiple_task":
            return "VA assigned multiple task"
        elif instance.status == "va_processing_multiple_task":
            return "VA processing multiple task"
        elif instance.status == "va_complete_multiple_task":
            return "VA complete multiple task"
        elif instance.status == "for_quality_review_multiple_task":
            return "For quality review multiple task"


class JobOrderGeneralAnalyticsSerializer(serializers.ModelSerializer):
    client = serializers.CharField(source="client.user.user_full_name")

    class Meta:
        model = JobOrderGeneralAnalytics
        fields = ("id", "month", "month_year", "client", "job_count")