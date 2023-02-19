from rest_framework import viewsets, permissions, generics

from apps.gpg.models import BuyerList

from apps.gpg.serializers import BuyerListSerializer

__all__ = ["BuyerListViewSet"]


class BuyerListViewSet(viewsets.ModelViewSet):
    serializer_class = BuyerListSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = BuyerList.objects.all()
