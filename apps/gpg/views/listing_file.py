from rest_framework import viewsets, permissions, generics

from apps.gpg.models import ListingFile

from apps.gpg.serializers import ListingFileSerializer

__all__ = ["ListingFileViewSet"]


class ListingFileViewSet(viewsets.ModelViewSet):
    serializer_class = ListingFileSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = ListingFile.objects.all()
