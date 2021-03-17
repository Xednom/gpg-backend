from rest_framework import serializers

from apps.gpg.models import (
    JobOrderCategory,
    CommentByApn,
    PropertyDetail,
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


class PropertyDetailSerializer(serializers.ModelSerializer):
    client_ = serializers.SerializerMethodField()
    client_code = serializers.SerializerMethodField()
    staff_ = serializers.SerializerMethodField()

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
            "price_status",
            "property_status",
            "category",
            "size",
            "asking_price",
            "cash_terms",
            "finance_terms",
            "other_terms",
            "notes",
            "ad_details",
            "notes_client_side",
            "notes_va_side",
            "notes_management_side",
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
    model = CategoryType
    fields = ("category",)


class ApnCommentSerializer(serializers.ModelSerializer):
    commenter = serializers.SerializerMethodField()

    class Meta:
        model = CommentByApn
        fields = (
            "propert_details",
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

    class Meta:
        model = JobOrderCategory
        fields = (
            "ticket_number",
            "client",
            "staff",
            "category",
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
