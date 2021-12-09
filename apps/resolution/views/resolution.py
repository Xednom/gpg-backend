from django.contrib.auth import get_user_model

from apps.resolution.models.resolution import Category
from rest_framework import viewsets, permissions, generics, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

from apps.resolution.models import Resolution, Category
from apps.resolution.serializers import ResolutionSerializer, CategorySerializer

User = get_user_model()


__all__ = ("ResolutionViewSet", "CategoryListView")


class CategoryListView(generics.ListAPIView):
    """
    List all categories.
    """

    serializer_class = CategorySerializer
    permissin_classes = (permissions.IsAuthenticated,)
    queryset = Category.objects.all()


class ResolutionViewSet(viewsets.ModelViewSet):
    serializer_class = ResolutionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        users = User.objects.filter(username=user)
        if user:
            return Resolution.objects.select_related("category", "assigned_to").filter(
                client__user__in=users
            ) or Resolution.objects.select_related(
                "category", "assigned_to"
            ).filter(
                assigned_to__user__in=users
            )
