from sqlite3 import Time, Timestamp
from django.db import models

from apps.core.models import TimeStamped


__all__ = ("Thread", "Comment", "Reply")


class Thread(TimeStamped):
    title = models.CharField(max_length=250)
    content = models.TextField()
    author = models.ForeignKey(
        "authentication.User", related_name="threads", on_delete=models.CASCADE
    )
    staff_carbon_copy = models.ManyToManyField(
        "authentication.Staff",
        blank=True,
    )
    client_carbon_copy = models.ManyToManyField(
        "authentication.Client",
        blank=True,
    )
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["-id"]
        verbose_name = "Thread"
        verbose_name_plural = "Threads"

    def __str__(self):
        return self.title


class Comment(TimeStamped):
    thread = models.ForeignKey(
        Thread, related_name="thread_comments", on_delete=models.CASCADE
    )
    author = models.ForeignKey(
        "authentication.User", related_name="comment_authors", on_delete=models.CASCADE
    )
    comment = models.TextField()

    class Meta:
        ordering = ["-id"]
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    def __str__(self):
        return self.content


class Reply(TimeStamped):
    comment = models.ForeignKey(
        Comment, related_name="comment_replies", on_delete=models.CASCADE
    )
    author = models.ForeignKey(
        "authentication.User", related_name="reply_authors", on_delete=models.CASCADE
    )
    content = models.TextField()

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Reply"
        verbose_name_plural = "Replies"

    def __str__(self):
        return f"{self.author}'s reply to {self.comment}"
