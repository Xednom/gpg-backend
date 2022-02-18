from django.db.models import Q
from django.contrib.auth import get_user_model

from rest_framework import viewsets, permissions, generics
from rest_framework.generics import get_object_or_404

from apps.authentication.models import Client, Staff
from apps.forum.models import Thread, Comment, Reply
from apps.forum.serializers import ThreadSerializer, CommentSerializer, ReplySerializer

from notifications.signals import notify


User = get_user_model()


__all__ = ("ThreadViewSet", "CommentView")


class ThreadViewSet(viewsets.ModelViewSet):
    serializer_class = ThreadSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        current_user = self.request.user
        client = Client.objects.filter(user=current_user)
        staff = Staff.objects.filter(user=current_user)
        queryset = []
        if client:
            queryset = (
                Thread.objects.select_related("author")
                .prefetch_related("staff_carbon_copy", "client_carbon_copy")
                .filter(Q(author=current_user) | Q(client_carbon_copy__in=client))
            )
        elif staff:
            queryset = (
                Thread.objects.select_related("author")
                .prefetch_related("staff_carbon_copy", "client_carbon_copy")
                .filter(Q(author=current_user) | Q(staff_carbon_copy__in=staff))
            )
        return queryset


class CommentView(generics.CreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Comment.objects.select_related("thread", "author").all()

    def perform_create(self, serializer):
        author = self.request.user
        thread_id = self.kwargs.get("id")
        thread = get_object_or_404(Thread, id=thread_id)
        serializer.save(author=author, thread=thread)
