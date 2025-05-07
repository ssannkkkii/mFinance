from django.urls import path
from .views import CreateTransactionView, ListTransactionsView

urlpatterns = [
    path("create/", CreateTransactionView.as_view()),
    path("list/", ListTransactionsView.as_view()),
]
