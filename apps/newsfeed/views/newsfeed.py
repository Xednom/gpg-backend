from post_office import mail
from rest_framework import viewsets, permissions, generics, filters
from rest_framework.generics import get_object_or_404

from django.db.models import Q
from django.contrib.auth import get_user_model

from apps.authentication.models import Staff, Client
from apps.newsfeed.models import NewsFeed, NewsFeedComment
from apps.newsfeed.serializers import NewsFeedSerializer, NewsfeedCommentSerializer


User = get_user_model()


__all__ = ("NewsFeedViewSet", "CreateNewsFeedComment")


class NewsFeedViewSet(viewsets.ModelViewSet):
    serializer_class = NewsFeedSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        clients = User.objects.filter(
            Q(username=user),
            Q(designation_category="new_client")
            | Q(designation_category="current_client")
            | Q(designation_category="affiliate_partner"),
        )
        staffs = User.objects.filter(Q(username=user), Q(designation_category="staff"))
        if clients:
            newsfeed = NewsFeed.objects.filter(
                Q(publish_to="client") | Q(publish_to="both")
            )
            return newsfeed
        elif staffs:
            newsfeed = NewsFeed.objects.filter(
                Q(publish_to="staff") | Q(publish_to="both")
            )
            return newsfeed


class CreateNewsFeedComment(generics.CreateAPIView):
    serializer_class = NewsfeedCommentSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = NewsFeedComment.objects.select_related("newsfeed", "user").all()

    def perform_create(self, serializer):
        user = self.request.user
        newsfeed_id = self.kwargs.get("id")
        newsfeed = get_object_or_404(NewsFeed, id=newsfeed_id)
        serializer.save(user=user, newsfeed=newsfeed)
