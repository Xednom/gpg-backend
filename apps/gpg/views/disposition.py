from rest_framework import viewsets, permissions, generics

from apps.gpg.models import Disposition

from apps.gpg.serializers import DispositionSerializer

__all__ = ["DispositionViewSet"]


class DispositionViewSet(viewsets.ModelViewSet):
    serializer_class = DispositionSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Disposition.objects.all()
