from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer

from apps.authentication.models import Client, Staff

from apps.gpg.models import (
    JobOrderCategory,
    CommentByApn,
    PropertyDetail,
    PropertyPrice,
    CategoryType,
    Deadline,
    State,
    County,
    PropertyDetailFile,
)

__all__ = (
    "CommentByApnSerializer",
    "PropertyDetailSerializer",
    "PropertyPriceSerializer",
    "CategoryTypeSerializer",
    "JobOrderCategorySerializer",
    "ApnCommentSerializer",
    "DeadlineSerializer",
    "StateSerializer",
    "CountySerializer",
    "PropertyDetailFileSerializer",
)


class CommentByApnSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentByApn
        fields = ("property_details", "user", "comment", "comment_created_at")


class PropertyPriceSerializer(WritableNestedModelSerializer):
    property_detail = serializers.PrimaryKeyRelatedField(
        queryset=PropertyDetail.objects.all(), required=False, allow_null=True
    )

    class Meta:
        model = PropertyPrice
        fields = (
            "id",
            "property_detail",
            "user",
            "asking_price",
            "cash_terms",
            "finance_terms",
            "other_terms",
            "price_status",
            "notes",
            "updated_info",
        )


class PropertyDetailFileSerializer(WritableNestedModelSerializer):
    property_detail = serializers.PrimaryKeyRelatedField(
        queryset=PropertyDetail.objects.all(), allow_null=True, required=False
    )

    class Meta:
        model = PropertyDetailFile
        fields = ("id", "property_detail", "details", "url", "description")


class PropertyDetailSerializer(WritableNestedModelSerializer):
    client = serializers.SlugRelatedField(
        slug_field="client_code", queryset=Client.objects.all()
    )
    client_ = serializers.SerializerMethodField()
    client_code = serializers.SerializerMethodField()
    staff_ = serializers.SerializerMethodField()
    client_email = serializers.CharField(required=False, allow_null=True)
    staff_email = serializers.CharField(required=False, allow_null=True)
    property_price_statuses = PropertyPriceSerializer(
        many=True, allow_null=True, required=False
    )
    property_detail_files = PropertyDetailFileSerializer(
        many=True, allow_null=True, required=False
    )

    class Meta:
        model = PropertyDetail
        fields = (
            "id",
            "created_at",
            "ticket_number",
            "client",
            "client_code",
            "client_",
            "staff",
            "staff_",
            "apn",
            "client_email",
            "staff_email",
            "county",
            "state",
            "property_status",
            "size",
            "property_owner",
            "company_name",
            "phone",
            "email",
            "website_url",
            "file_storage",
            "notes_client_side",
            "notes_va_side",
            "notes_management_side",
            "property_price_statuses",
            "property_detail_files",
        )

    def get_client_(self, instance):
        if instance.client is None:
            return "Management on process"
        else:
            return instance.client.client_name

    def get_client_code(self, instance):
        if instance.client is None:
            return "Management on process"

        else:
            return instance.client.client_code

    def get_staff_(self, instance):
        if instance.staff is None:
            return "Processing a VA"


class CategoryTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryType
        fields = ("category",)


class ApnCommentSerializer(serializers.ModelSerializer):
    commenter = serializers.SerializerMethodField()
    user_type = serializers.SerializerMethodField()
    created_at = serializers.DateTimeField(required=False, allow_null=True)

    class Meta:
        model = CommentByApn
        fields = (
            "job_order_category",
            "user",
            "comment",
            "commenter",
            "user_type",
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
        else:
            client_code = [client.client_code for client in get_client_code]
            client_code = "".join(client_code)
            return client_code


class JobOrderCategorySerializer(serializers.ModelSerializer):
    client = serializers.SlugRelatedField(
        slug_field="client_code", queryset=Client.objects.all()
    )
    job_order_category_comments = ApnCommentSerializer(
        many=True, required=False, allow_null=True
    )
    category = serializers.SlugRelatedField(
        slug_field="category", queryset=CategoryType.objects.all()
    )
    property_detail = serializers.SlugRelatedField(
        slug_field="apn", queryset=PropertyDetail.objects.all()
    )
    deadline = serializers.SlugRelatedField(
        slug_field="deadline", queryset=Deadline.objects.all()
    )
    property_detail_ticket = serializers.SerializerMethodField()
    status_ = serializers.SerializerMethodField()
    category_ = serializers.SerializerMethodField()
    client_code = serializers.SerializerMethodField()

    class Meta:
        model = JobOrderCategory
        fields = (
            "id",
            "created_at",
            "ticket_number",
            "property_detail",
            "property_detail_ticket",
            "client",
            "client_email",
            "client_code",
            "staff",
            "staff_email",
            "category",
            "category_",
            "status",
            "status_",
            "due_date",
            "date_completed",
            "job_description",
            "url_of_the_completed_jo",
            "notes_va",
            "notes_management",
            "total_time_consumed",
            "job_order_category_comments",
            "deadline",
        )

    def get_category_(self, instance):
        if instance.category.category is None:
            return "No Category exist as of now"
        else:
            return f"{instance.category.category}"

    def get_client_code(self, instance):
        if instance.client is None:
            return "Client being process"
        else:
            return f"{instance.client.client_code}"

    def get_property_detail_ticket(self, instance):
        if instance.property_detail:
            return instance.property_detail.ticket_number

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


class DeadlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deadline
        fields = (
            "id",
            "deadline",
        )


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = ("name",)


class CountySerializer(serializers.ModelSerializer):
    state = serializers.SlugRelatedField(
        slug_field="name", queryset=State.objects.all()
    )

    class Meta:
        model = County
        fields = ("name", "state")
