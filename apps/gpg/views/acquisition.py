from rest_framework import viewsets, permissions, generics, filters, status
from rest_framework.views import APIView
from rest_framework.response import Response

from apps.gpg.models import Acquisition

from apps.gpg.serializers import AcquisitionSerializer

__all__ = ["AcquisitionViewSet", "SaveAcquisitions"]


class AcquisitionViewSet(viewsets.ModelViewSet):
    serializer_class = AcquisitionSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ["property_detail__id"]
    queryset = Acquisition.objects.all()


class SaveAcquisitions(APIView):
    def post(self, request, format=None):
        data = request.data
        for item in data:
            serializer = AcquisitionSerializer(data=item)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        return Response({"status": True}, status.HTTP_200_OK)
