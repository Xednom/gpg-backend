from rest_framework import viewsets, permissions
from rest_framework.response import Response

from notifications.models import Notification
from apps.gpg_notifications.serializers import NotificationSerializer


class NotificationViewSet(viewsets.ModelViewSet):
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return (
            Notification.objects.select_related(
                "recipient",
                "actor_content_type",
                "target_content_type",
                "action_object_content_type",
            )
            .filter(recipient=user)
            .unread()
        )
    
    def perform_update(self, serializer):
        serializer.save(unread=False)
