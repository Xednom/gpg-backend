from rest_framework import viewsets, permissions, generics, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

from apps.resolution.models import Resolution
from apps.resolution.serializers import ResolutionSerializer


__all__ = ("ResolutionViewSet",)


class ResolutionViewSet(viewsets.ModelViewSet):
    serializer_class = ResolutionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Resolution.objects.select_related("category", "assigned_to").filter(
            assigned_to__user=user
        )
