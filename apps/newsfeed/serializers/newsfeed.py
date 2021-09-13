from rest_framework import serializers

from apps.newsfeed.models import NewsFeed, NewsFeedComment


__all__ = ("NewsFeedSerializer",)


class NewsFeedSerializer(serializers.ModelSerializer):

    class Meta:
        model = NewsFeed
        fields = (
            "title",
            "body",
            "publish_to"
        )