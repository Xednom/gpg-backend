from rest_framework import viewsets, permissions, generics

from apps.gpg.models import SellerList

from apps.gpg.serializers import SellerListSerializer

__all__ = ["SellerListViewSet"]


class SellerListViewSet(viewsets.ModelViewSet):
    serializer_class = SellerListSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = SellerList.objects.all()