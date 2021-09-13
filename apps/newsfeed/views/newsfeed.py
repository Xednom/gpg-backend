from post_office import mail
from rest_framework import viewsets, permissions, generics, filters

from django.db.models import Q
from django.contrib.auth import get_user_model

from apps.authentication.models import Staff, Client
from apps.newsfeed.models import NewsFeed
from apps.newsfeed.serializers import NewsFeedSerializer


User = get_user_model()


__all__ = ("NewsFeedViewSet",)


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
        staffs = User.objects.filter(
            Q(username=user),
            Q(designation_category="staff")
        )
        if clients:
            newsfeed = NewsFeed.objects.filter(publish_to="client")
            return newsfeed
        elif staffs:
            newsfeed = NewsFeed.objects.filter(publish_to="staff")
            return newsfeed
        else:
            newsfeed = NewsFeed.objets.filter(publish_to="both")
            return newsfeed
        
