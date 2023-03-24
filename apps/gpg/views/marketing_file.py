from rest_framework import viewsets, permissions, generics, filters, status
from rest_framework.views import APIView
from rest_framework.response import Response

from apps.gpg.models import MarketingFile

from apps.gpg.serializers import MarketingFileSerializer

__all__ = ["MarketingFileViewSet", "SaveMarketings"]


class MarketingFileViewSet(viewsets.ModelViewSet):
    serializer_class = MarketingFileSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ["property_detail__id"]
    queryset = MarketingFile.objects.all()


class SaveMarketings(APIView):
    def post(self, request, format=None):
        data = request.data
        for item in data:
            serializer = MarketingFileSerializer(data=item)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        return Response({"status": True}, status.HTTP_200_OK)
