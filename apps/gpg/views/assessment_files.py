from rest_framework import viewsets, permissions, generics, filters, status
from rest_framework.views import APIView
from rest_framework.response import Response

from apps.gpg.models import AssessmentFile

from apps.gpg.serializers import AssessmentFileSerializer

__all__ = ["AssessmentFileViewSet", "SaveAssessments"]


class AssessmentFileViewSet(viewsets.ModelViewSet):
    serializer_class = AssessmentFileSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = AssessmentFile.objects.all()


class SaveAssessments(APIView):
    def post(self, request, format=None):
        data = request.data
        for item in data:
            serializer = AssessmentFileSerializer(data=item)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        return Response({"status": True}, status.HTTP_200_OK)
