from django.contrib.auth import get_user_model

from rest_framework import viewsets, permissions, generics
from rest_framework.generics import get_object_or_404

from apps.forum.models import Thread, Comment, Reply
from apps.forum.serializers import ThreadSerializer, CommentSerializer, ReplySerializer

from notifications.signals import notify


User = get_user_model()


__all__ = ("ThreadViewSet",)


class ThreadViewSet(viewsets.ModelViewSet):
    serializer_class = ThreadSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        current_user = self.request.user
        clients = User.objects.filter(username=current_user)
        staffs = User.objects.filter(username=current_user)
        client = clients.all()
        staff = staffs.all()

        if current_user:
            queryset = Thread.objects.select_related(
                "author"
            ).prefetch_related("staff_carbon_copy", "client_carbon_copy").filter(
                author__in=client
            ) or Thread.objects.select_related(
                "author"
            ).prefetch_related("staff_carbon_copy", "client_carbon_copy").filter(
                author__username__in=staff
            ).exclude(
                is_active=False
            )
            return queryset
        else:
            queryset = Thread.objects.all()
            return queryset