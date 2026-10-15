from django.db import models

# Create your models here.




from django.contrib.auth.models import User
from django.db import models


class Expense(models.Model):

    CATEGORY_CHOICES = [
        ("FOOD", "Food"),
        ("TRAVEL", "Travel"),
        ("SHOPPING", "Shopping"),
        ("BILLS", "Bills"),
        ("HEALTH", "Health"),
        ("ENTERTAINMENT", "Entertainment"),
        ("OTHER", "Other"),
    ]

    PRIORITY_CHOICES = [
        ("need", "need"),
        ("want", "want"),
        
    ]



    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="expenses"
    )

    title = models.CharField(max_length=100)

    amount = models.DecimalField(max_digits=10, decimal_places=2)

    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES
    )

    priority = models.CharField(
        max_length=10,
        choices=PRIORITY_CHOICES,
        default="need"
    )

    PAYMENT_METHOD_CHOICES=(
        ("cash","cash"),
        ("upi","upi")
    )

    payment_method = models.CharField(max_length=200,choices=PAYMENT_METHOD_CHOICES,default="upi")

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):

        return f"{self.title}"