from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer

from apps.gpg.models import (
    JobOrderCategory,
    CommentByApn,
    PropertyDetail,
    PropertyPrice,
    CategoryType,
)

__all__ = (
    "CommentByApnSerializer",
    "PropertyDetailSerializer",
    "CategoryTypeSerializer",
    "JobOrderCategorySerializer",
    "ApnCommentSerializer"
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


class PropertyPriceSerializer(serializers.ModelSerializer):
    property_detail = serializers.PrimaryKeyRelatedField(queryset=PropertyDetail.objects.all(), required=False, allow_null=True)
    
    class Meta:
        model = PropertyPrice
        fields = (
            "property_detail",
            "user",
            "asking_price",
            "cash_terms",
            "finance_terms",
            "other_terms",
            "price_status",
            "notes",
            "updated_info"
        )


class PropertyDetailSerializer(WritableNestedModelSerializer):
    client_ = serializers.SerializerMethodField()
    client_code = serializers.SerializerMethodField()
    staff_ = serializers.SerializerMethodField()
    property_price_statuses = PropertyPriceSerializer(many=True, allow_null=True, required=False)

    class Meta:
        model = PropertyDetail
        fields = (
            "ticket_number",
            "client",
            "client_code",
            "client_",
            "staff",
            "staff_",
            "apn",
            "county",
            "state",
            "property_status",
            "size",
            "company_name",
            "phone",
            "email",
            "website_url",
            "ad_details",
            "notes_client_side",
            "notes_va_side",
            "notes_management_side",
            "property_price_statuses",
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
        fields = (
            "job_order_category",
            "user",
            "comment",
            "commenter"
        )

    def get_commenter(self, instance):
        if instance.user.designation_category == "staff":
            return "Virtual Assistant"
        else:
            return "Client"


class JobOrderCategorySerializer(serializers.ModelSerializer):
    job_order_category_comments = ApnCommentSerializer(many=True, required=False, allow_null=True)
    category = serializers.SlugRelatedField(slug_field="category", queryset=CategoryType.objects.all())
    category_ = serializers.SerializerMethodField()
    client_code = serializers.SerializerMethodField()

    class Meta:
        model = JobOrderCategory
        fields = (
            "id",
            "ticket_number",
            "client",
            "client_code",
            "staff",
            "category",
            "category_",
            "status",
            "due_date",
            "date_completed",
            "job_description",
            "completed_url_work",
            "notes_va",
            "notes_management",
            "total_time_consumed",
            "job_order_category_comments"
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
