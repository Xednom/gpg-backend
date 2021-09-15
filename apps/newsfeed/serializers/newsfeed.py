from rest_framework import serializers

from apps.authentication.models import Staff, Client
from apps.newsfeed.models import NewsFeed, NewsFeedComment


__all__ = ("NewsFeedSerializer", "NewsfeedCommentSerializer")


class NewsfeedCommentSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(required=False, allow_null=True)
    commenter = serializers.SerializerMethodField()
    user_type = serializers.SerializerMethodField()

    class Meta:
        model = NewsFeedComment
        fields = (
            "newsfeed",
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


class NewsFeedSerializer(serializers.ModelSerializer):
    news_feed_comments = NewsfeedCommentSerializer(
        many=True, required=False, allow_null=True
    )

    class Meta:
        model = NewsFeed
        fields = ("id", "title", "body", "publish_to", "news_feed_comments")
