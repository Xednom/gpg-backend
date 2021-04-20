from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer

from apps.authentication.models import Client

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
)


class CommentByApnSerializer(serializers.ModelSerializer):
    commenter = serializers.SerializerMethodField()

    class Meta:
        model = CommentByApn
        fields = (
            "property_details",
            "user",
            "comment",
            "commenter",
        )

    def get_commenter(self, instance):
        if instance.user.designation_category == "staff":
            return "Virtual Assistant"
        else:
            return "Client"


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
            "company_name",
            "phone",
            "email",
            "website_url",
            "file_storage",
            "notes_client_side",
            "notes_va_side",
            "notes_management_side",
            "property_price_statuses",
            "property_detail_files"
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

    class Meta:
        model = CommentByApn
        fields = ("job_order_category", "user", "comment", "commenter")

    def get_commenter(self, instance):
        if instance.user.designation_category == "staff":
            return "Virtual Assistant"
        else:
            return "Client"


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
    category_ = serializers.SerializerMethodField()
    client_code = serializers.SerializerMethodField()

    class Meta:
        model = JobOrderCategory
        fields = (
            "id",
            "ticket_number",
            "property_detail",
            "client",
            "client_email",
            "client_code",
            "staff",
            "staff_email",
            "category",
            "category_",
            "status",
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
