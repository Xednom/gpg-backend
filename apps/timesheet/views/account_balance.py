from django.conf import settings

from django.contrib.auth import get_user_model

from rest_framework.decorators import action
from rest_framework import viewsets, permissions, generics, filters, status
from rest_framework.response import Response

from paypalcheckoutsdk.core import PayPalHttpClient, SandboxEnvironment
from paypalcheckoutsdk.orders import OrdersCaptureRequest

from apps.timesheet.models import AccountBalance
from apps.timesheet.serializers import (
    AccountBalanceSerializer,
    PaymentHistorySerializer,
)

User = get_user_model()


__all__ = ("AccountBalanceViewSet",)


class AccountBalanceViewSet(viewsets.ModelViewSet):
    serializer_class = AccountBalanceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        current_user = self.request.user
        user = User.objects.filter(username=current_user)

        if current_user:
            queryset = AccountBalance.objects.select_related("client").filter(
                client__user__in=user
            )
            return queryset

    @action(methods=["post"], detail=False, serializer_class=PaymentHistorySerializer)
    def checkout(self, *args, **kwargs):
        """
        Checkout
        """
        serializer = PaymentHistorySerializer(data=self.request.data)

        if serializer.is_valid():
            client_id = settings.PAYPAL_API_KEY_CLIENT_ID_SANDBOX
            client_secret = settings.PAYPAL_API_KEY_SECRET
            print(serializer.validated_data)

            # Create a Http client with environment that point to the PayPal sandbox
            client = PayPalHttpClient(
                environment=SandboxEnvironment(client_id, client_secret)
            )

            print(serializer)
            request = OrdersCaptureRequest(serializer.validated_data["payment_id"])
            response = client.execute(request)

            try:
                if response.result.status == "COMPLETED":
                    serializer.client_name = self.request.user
                    serializer.save(
                        payment_channel="Paypal",
                        transaction_number=response.result.id,
                        client=self.request.user,
                        client_name=self.request.user.user_full_name,
                    )
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
            except:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=["put"], detail=False, serializer_class=AccountBalanceSerializer)
    def update_balance(self, *args, **kwargs):
        """
        Update Balance
        """
        serializer = AccountBalanceSerializer(data=self.request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
