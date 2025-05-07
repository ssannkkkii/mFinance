from django.urls import path
from .views import (
    SendOTPView,
    VerifyOTPView,
    CompleteProfileView,
    UserProfileView,
    LogoutView,
)

urlpatterns = [
    path("send-otp/", SendOTPView.as_view()),
    path("verify-otp/", VerifyOTPView.as_view()),
    path("complete-profile/", CompleteProfileView.as_view()),
    path("profile/", UserProfileView.as_view()),
    path("logout/", LogoutView.as_view()),
]
