from django.db import models
from users.models import BankCard

class Transaction(models.Model):
    CATEGORY_CHOICES = [
    ("alcohol", "Alcohol"),
    ("food", "Food"),
    ("transport", "Transport"),
    ("entertainment", "Entertainment"),
    ("groceries", "Groceries"),
    ("health", "Health"),
    ("education", "Education"),
    ("clothing", "Clothing"),
    ("bills", "Bills & Utilities"),
    ("subscriptions", "Subscriptions"),
    ("electronics", "Electronics"),
    ("home", "Home & Furniture"),
    ("sports", "Sports & Outdoors"),
    ("travel", "Travel"),
    ("gifts", "Gifts"),
    ("kids", "Kids"),
    ("pets", "Pets"),
    ("charity", "Charity"),
    ("cash", "Cash Withdrawal"),
    ("other", "Other"),
    ]

    card = models.ForeignKey(BankCard, on_delete=models.CASCADE, related_name="transactions")
    title = models.CharField(max_length=100)  # Назва: "Пиво Джоні"
    place = models.CharField(max_length=100)  # Де купив: "Рукавичка"
    place_category = models.CharField(max_length=50)  # Категорія місця: "Супермаркет"
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.amount}$ at {self.place}"
