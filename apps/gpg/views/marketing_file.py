from rest_framework import viewsets, permissions, generics

from apps.gpg.models import MarketingFile

from apps.gpg.serializers import MarketingFileSerializer

__all__ = ["MarketingFileViewSet"]


class MarketingFileViewSet(viewsets.ModelViewSet):
    serializer_class = MarketingFileSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = MarketingFile.objects.all()
