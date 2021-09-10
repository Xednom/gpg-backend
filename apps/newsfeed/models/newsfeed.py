from django.db import models

from django.contrib.auth import get_user_model

from apps.core.models import TimeStamped
from django_bleach.models import BleachField


User = get_user_model()


__all__ = ("NewsFeed", "NewsFeedComment")


class PublishTo(models.TextChoices):
    staff = "staff", ("Staff")
    client = "client", ("Client")
    both = "both", ("Both")


class NewsFeed(TimeStamped):
    title = models.CharField(max_length=250)
    body = BleachField()
    publish_to = models.CharField(
        max_length=100,
        choices=PublishTo.choices,
        default=PublishTo.both,
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"{self.title}"


class NewsFeedComment(TimeStamped):
    newsfeed = models.ForeignKey(
        NewsFeed,
        related_name="news_feed_comments",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    user = models.ForeignKey(
        User,
        related_name="user_news_feeds",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    comment = models.TextField()

    class Meta:
        ordering = ["-created_at"]
