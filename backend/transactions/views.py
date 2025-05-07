from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from .models import Transaction
from .serializers import TransactionSerializer

class CreateTransactionView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        user = request.user
        if not hasattr(user, "bank_card"):
            return Response({"error": "User has no bank card."}, status=400)

        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            transaction = serializer.save(card=user.bank_card)

            user.bank_card.balance -= transaction.amount
            user.bank_card.save()

            return Response(TransactionSerializer(transaction).data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ListTransactionsView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        if not hasattr(user, "bank_card"):
            return Response({"error": "User has no bank card."}, status=400)

        transactions = user.bank_card.transactions.all().order_by("-created_at")
        serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data)
