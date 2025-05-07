from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import CustomUser, BankCard
from .serializers import (
    SendOTPSerializer,
    VerifyOTPSerializer,
    CompleteProfileSerializer,
    UserProfileSerializer,
    BankCardSerializer,
    TopUpBalanceSerializer
)
from rest_framework_simplejwt.tokens import RefreshToken
from .utils import generate_card_number, generate_cvv


def set_jwt_cookie(response, user):
    refresh = RefreshToken.for_user(user)
    access_token = str(refresh.access_token)
    refresh_token = str(refresh)

    response.set_cookie(
        key="access",
        value=access_token,
        httponly=True,
        secure=False,       # У продакшені поставити True
        samesite="Lax",
        path="/"
    )
    response.set_cookie(
        key="refresh",
        value=refresh_token,
        httponly=True,
        secure=False,
        samesite="Lax",
        path="/"
    )

class SendOTPView(APIView):
    def post(self, request):
        serializer = SendOTPSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"detail": "OTP sent"})

class VerifyOTPView(APIView):
    def post(self, request):
        serializer = VerifyOTPSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        response = Response({"detail": "OTP verified"})
        set_jwt_cookie(response, user)
        return response

class CompleteProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        user = request.user
        first_name = request.data.get("first_name")
        last_name = request.data.get("last_name")

        if not first_name or not last_name:
            return Response({"error": "First name and last name are required."}, status=400)

        user.first_name = first_name
        user.last_name = last_name
        user.is_profile_completed = True
        user.save()

        if not hasattr(user, "card"):
            card = BankCard.objects.create(
                user=user,
                card_number=generate_card_number(),
                cvv=generate_cvv(),
            )
            return Response({
                "message": "Profile completed and card created.",
                "card": {
                    "card_number": card.card_number,
                    "cvv": card.cvv,
                    "expiry_date": card.expiry_date,
                    "balance": card.balance,
                }
            }, status=200)

        return Response({"message": "Profile already completed."}, status=200)

class UserProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data)

class LogoutView(APIView):
    def post(self, request):
        response = Response({"detail": "Logged out"}, status=status.HTTP_200_OK)
        response.delete_cookie("access")
        response.delete_cookie("refresh")
        return response
    
class BankCardView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        serializer = BankCardSerializer(request.user.bank_card)
        return Response(serializer.data)


class TopUpBalanceView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = TopUpBalanceSerializer(data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        card = serializer.save()
        return Response({"detail": f"Balance topped up. New balance: {card.balance}"})