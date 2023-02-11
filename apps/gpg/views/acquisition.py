from rest_framework import viewsets, permissions, generics

from apps.gpg.models import Acquisition

from apps.gpg.serializers import AcquisitionSerializer

__all__ = ["AcquisitionViewSet"]


class AcquisitionViewSet(viewsets.ModelViewSet):
    serializer_class = AcquisitionSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Acquisition.objects.all()
