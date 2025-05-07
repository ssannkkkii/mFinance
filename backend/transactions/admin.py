from django.contrib import admin
from .models import Transaction
from users.models import BankCard  

class TransactionAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "amount", "place", "place_category", "card", "created_at")
    list_filter = ("category", "created_at")
    search_fields = ("title", "place", "place_category", "card__user__phone")
    ordering = ("-created_at",)

    fieldsets = (
        (None, {
            "fields": ("title", "category", "amount", "place", "place_category", "card")
        }),
        ("Timestamps", {
            "fields": ("created_at",),
            "classes": ("collapse",),
        }),
    )

admin.site.register(Transaction, TransactionAdmin)
