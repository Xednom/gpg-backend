from rest_framework import viewsets, permissions, generics, filters, status
from rest_framework.views import APIView
from rest_framework.response import Response

from apps.gpg.models import ListingFile, ListingStatus

from apps.gpg.serializers import ListingFileSerializer, ListingStatusSerializer

__all__ = ["ListingFileViewSet", "ListingStatusViewSet", "SaveListings"]


class ListingStatusViewSet(viewsets.ModelViewSet):
    serializer_class = ListingStatusSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = ListingStatus.objects.all()


class ListingFileViewSet(viewsets.ModelViewSet):
    serializer_class = ListingFileSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ["property_detail__id"]
    queryset = ListingFile.objects.all()


class SaveListings(APIView):
    def post(self, request, format=None):
        data = request.data
        for item in data:
            serializer = ListingFileSerializer(data=item)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        return Response({"status": True}, status.HTTP_200_OK)
