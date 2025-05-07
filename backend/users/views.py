from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import CustomUser
from .serializers import (
    SendOTPSerializer,
    VerifyOTPSerializer,
    CompleteProfileSerializer,
    UserProfileSerializer,
)
from rest_framework_simplejwt.tokens import RefreshToken

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
        serializer = CompleteProfileSerializer(instance=request.user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"detail": "Profile completed"})

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
