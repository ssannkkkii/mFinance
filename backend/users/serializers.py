from rest_framework import serializers
from .models import CustomUser, OTP, BankCard
from django.utils import timezone
from datetime import timedelta
import random

class SendOTPSerializer(serializers.Serializer):
    phone = serializers.CharField()

    def create(self, validated_data):
        phone = validated_data["phone"]
        code = f"{random.randint(100000, 999999)}"
        OTP.objects.create(phone=phone, code=code)
        print(f"[OTP DEBUG] Code for {phone} is {code}")  # інтегруй SMS API тут
        return {"phone": phone}

class VerifyOTPSerializer(serializers.Serializer):
    phone = serializers.CharField()
    code = serializers.CharField()

    def validate(self, data):
        phone = data["phone"]
        code = data["code"]
        time_threshold = timezone.now() - timedelta(minutes=5)
        otp_qs = OTP.objects.filter(phone=phone, code=code, created_at__gte=time_threshold)
        if not otp_qs.exists():
            raise serializers.ValidationError("Invalid or expired OTP")

        user, _ = CustomUser.objects.get_or_create(phone=phone)
        return {"user": user}

class CompleteProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["first_name", "last_name"]

    def update(self, instance, validated_data):
        instance.first_name = validated_data["first_name"]
        instance.last_name = validated_data["last_name"]
        instance.is_profile_completed = True
        instance.save()
        return instance

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["phone", "first_name", "last_name", "is_profile_completed"]

class BankCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankCard
        fields = ["card_number", "cvv", "expiry_date", "balance"]


class TopUpBalanceSerializer(serializers.Serializer):
    amount = serializers.DecimalField(max_digits=12, decimal_places=2)

    def validate_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError("Amount must be greater than zero.")
        return value

    def save(self, **kwargs):
        user = self.context["request"].user
        card = user.bank_card
        card.balance += self.validated_data["amount"]
        card.save()
        return card