from rest_framework import viewsets, permissions, generics, filters, status
from rest_framework.views import APIView
from rest_framework.response import Response

from apps.gpg.models import BuyerList

from apps.gpg.serializers import BuyerListSerializer

__all__ = ["BuyerListViewSet", "SaveBuyerLists"]


class BuyerListViewSet(viewsets.ModelViewSet):
    serializer_class = BuyerListSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ["property_detail__id"]
    queryset = BuyerList.objects.all()


class SaveBuyerLists(APIView):
    def post(self, request, format=None):
        data = request.data
        for item in data:
            serializer = BuyerListSerializer(data=item)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        return Response({"status": True}, status.HTTP_200_OK)
