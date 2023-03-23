from rest_framework import viewsets, permissions, generics, filters, status
from rest_framework.views import APIView
from rest_framework.response import Response

from apps.gpg.models import Disposition

from apps.gpg.serializers import DispositionSerializer

__all__ = ["DispositionViewSet", "SaveDispositions"]


class DispositionViewSet(viewsets.ModelViewSet):
    serializer_class = DispositionSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ["property_detail__id"]
    queryset = Disposition.objects.all()


class SaveDispositions(APIView):
    def post(self, request, format=None):
        data = request.data
        for item in data:
            serializer = DispositionSerializer(data=item)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        return Response({"status": True}, status.HTTP_200_OK)
