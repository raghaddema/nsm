from django.db import models

class Payment(models.Model):
    """نموذج أولي يمثل عملية دفع."""
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    method = models.CharField(max_length=50, default="بطاقة")

    class Meta:
        verbose_name = "Payment"
        verbose_name_plural = "Payments"

    def __str__(self):
        return f"دفعة بمبلغ {self.amount} ريال"
