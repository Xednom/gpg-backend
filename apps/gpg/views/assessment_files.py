from rest_framework import viewsets, permissions, generics

from apps.gpg.models import AssessmentFile

from apps.gpg.serializers import AssessmentFileSerializer

__all__ = ["AssessmentFileViewSet"]


class AssessmentFileViewSet(viewsets.ModelViewSet):
    serializer_class = AssessmentFileSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = AssessmentFile.objects.all()
