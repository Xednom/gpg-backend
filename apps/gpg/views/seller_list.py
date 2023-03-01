from rest_framework import viewsets, permissions, generics, filters, status
from rest_framework.views import APIView
from rest_framework.response import Response

from apps.gpg.models import SellerList

from apps.gpg.serializers import SellerListSerializer

__all__ = ["SellerListViewSet", "SaveSellerLists"]


class SellerListViewSet(viewsets.ModelViewSet):
    serializer_class = SellerListSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ["property_detail__id"]
    queryset = SellerList.objects.all()


class SaveSellerLists(APIView):
    def post(self, request, format=None):
        data = request.data
        for item in data:
            serializer = SellerListSerializer(data=item)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        return Response({"status": True}, status.HTTP_200_OK)
