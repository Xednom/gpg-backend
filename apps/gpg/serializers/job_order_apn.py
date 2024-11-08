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
    JobOrderCategoryAnalytics,
    JobOrderCategoryRating,
    JobOrderCategoryAgentScoring,
    SellerList,
    BuyerList,
    Acquisition,
    Disposition,
    AssessmentFile,
    MarketingFile,
    ListingFile,
)

from apps.gpg.serializers import (
    seller_list,
    buyer_list,
    acquisition,
    disposition,
    assessment_files,
    marketing_file,
    listing_file,
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
    "JobOrderApnAnalyticsSerializer",
    "JobOrderCategoryNotifSerializer",
)


class JobOrderCategoryAgentScoringSerializer(serializers.ModelSerializer):
    client = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all())
    job_order_category = serializers.SlugRelatedField(
        slug_field="ticket_number", queryset=JobOrderCategory.objects.all()
    )

    class Meta:
        model = JobOrderCategoryAgentScoring
        fields = (
            "id",
            "staff",
            "client",
            "job_order_category",
            "accuracy",
            "speed",
            "quality_of_work",
            "delivered_on_time",
            "delivery_note",
            "job_completed",
            "job_completed_note",
            "satisfied",
            "days_before_due_date",
            "days_after_due_date",
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
    property_detail_seller_lists = seller_list.SellerListSerializer(
        many=True, allow_null=True, required=False
    )
    property_detail_buyer_lists = buyer_list.BuyerListSerializer(
        many=True, allow_null=True, required=False
    )
    property_detail_acquisition = acquisition.AcquisitionSerializer(
        many=True, allow_null=True, required=False
    )
    property_detail_disposition = disposition.DispositionSerializer(
        many=True, allow_null=True, required=False
    )
    property_detail_assessment_files = assessment_files.AssessmentFileSerializer(
        many=True, allow_null=True, required=False
    )
    property_detail_marketing_file = marketing_file.MarketingFileSerializer(
        many=True, allow_null=True, required=False
    )
    property_detail_listing_file = listing_file.ListingFileSerializer(
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
            "property_complete_address",
            "property_detail_seller_lists",
            "property_detail_buyer_lists",
            "property_detail_acquisition",
            "property_detail_disposition",
            "property_detail_assessment_files",
            "property_detail_marketing_file",
            "property_detail_listing_file",
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
    created_at = serializers.DateField(required=False, allow_null=True)

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
        admin_user = "admin"
        if instance.user.designation_category == "staff":
            return staff_user
        elif instance.user.designation_category != "staff":
            return client_user
        else:
            return admin_user

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


class JobOrderCategoryRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobOrderCategoryRating
        fields = (
            "id",
            "client",
            "job_order",
            "rating",
            "comment",
        )


class JobOrderCategoryNotifSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobOrderCategory
        fields = ("ticket_number",)


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
    property_detail = serializers.PrimaryKeyRelatedField(
        queryset=PropertyDetail.objects.all(), required=False, allow_null=True
    )
    property_detail__apn = serializers.CharField(
        source="property_detail.apn", required=False, read_only=True
    )
    deadline = serializers.SlugRelatedField(
        slug_field="deadline", queryset=Deadline.objects.all()
    )
    job_category_ratings = JobOrderCategoryRatingSerializer(
        many=True, required=False, allow_null=True
    )
    job_order_category_scorings = JobOrderCategoryAgentScoringSerializer(
        many=True, required=False, allow_null=True
    )
    property_detail_ticket = serializers.SerializerMethodField()
    status_ = serializers.SerializerMethodField()
    category_ = serializers.SerializerMethodField()
    client_code = serializers.SerializerMethodField()
    job_rating = serializers.SerializerMethodField()

    class Meta:
        model = JobOrderCategory
        fields = (
            "id",
            "created_at",
            "ticket_number",
            "property_detail",
            "property_detail__apn",
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
            "job_category_ratings",
            "job_order_category_scorings",
            "job_rating",
            "deadline",
            "days_before_due_date",
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

    def get_job_rating(self, instance):
        get_job_category_rating = (
            JobOrderCategoryRating.objects.select_related().filter(
                job_order=instance.id
            )
        )
        if instance.job_category_ratings:
            job_rating = (rate.rating for rate in get_job_category_rating)
            return job_rating
        else:
            return "No rating yet"

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


class JobOrderApnAnalyticsSerializer(serializers.ModelSerializer):
    client = serializers.CharField(source="client.user.user_full_name")

    class Meta:
        model = JobOrderCategoryAnalytics
        fields = ("id", "month", "month_year", "client", "job_count")
