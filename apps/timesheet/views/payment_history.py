from datetime import datetime

from django.conf import settings

from django.contrib.auth import get_user_model

from rest_framework.decorators import action
from rest_framework import viewsets, permissions, generics, filters, status
from rest_framework.response import Response

from paypalcheckoutsdk.core import PayPalHttpClient, SandboxEnvironment, LiveEnvironment
from paypalcheckoutsdk.orders import OrdersCaptureRequest

from apps.timesheet.models import PaymentHistory
from apps.timesheet.serializers import PaymentHistorySerializer

User = get_user_model()

__all__ = ("PaymentHistoryViewSet",)


class PaymentHistoryViewSet(viewsets.ModelViewSet):
    serializer_class = PaymentHistorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        current_user = self.request.user
        user = User.objects.filter(username=current_user)

        if current_user:
            queryset = PaymentHistory.objects.select_related("client").filter(
                client__user__in=user
            )
            return queryset

    # TODO: this is for backend integration of Paypal(currently we have the frontend)
    # reason for commenting: use the frontend for secure transaction with paypal, this code block returns an error of duplicate orders.

    # def perform_create(self, serializer):
    #     serializer = PaymentHistorySerializer(data=self.request.data)

    #     if serializer.is_valid():
    #         client_id = settings.PAYPAL_API_KEY_CLIENT_ID_SANDBOX
    #         client_secret = settings.PAYPAL_API_KEY_SECRET_SANDBOX

    #         # Create a Http client with environment that point to the PayPal sandbox
    #         environment = SandboxEnvironment(client_id=client_id, client_secret=client_secret)
    #         client = PayPalHttpClient(environment)

    #         request = OrdersCaptureRequest(serializer.validated_data["payment_id"])
    #         response = client.execute(request)

    #         try:
    #             if response.result.status == "COMPLETED":
    #                 print(response.result)
    #                 serializer.save()
    #                 return Response(serializer.data, status=status.HTTP_201_CREATED)
    #         except:
    #             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
