from django.urls import path
from .views import (
    SendOTPView,
    VerifyOTPView,
    CompleteProfileView,
    UserProfileView,
    LogoutView,
    BankCardView,
    TopUpBalanceView
)

urlpatterns = [
    path("send-otp/", SendOTPView.as_view()),
    path("verify-otp/", VerifyOTPView.as_view()),
    path("complete-profile/", CompleteProfileView.as_view()),
    path("profile/", UserProfileView.as_view()),
    path("logout/", LogoutView.as_view()),
    path("bank-card/", BankCardView.as_view()),
    path("top-up/", TopUpBalanceView.as_view()),
]
