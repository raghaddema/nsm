from django.db import models


class Payment(models.Model):
    """نموذج يمثل عملية دفع داخل النظام."""

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="المبلغ المدفوع (ريال)"
    )
    payment_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name="تاريخ الدفع"
    )
    method = models.CharField(
        max_length=50,
        default="بطاقة",
        verbose_name="طريقة الدفع"
    )

    class Meta:
        verbose_name = "عملية دفع"
        verbose_name_plural = "عمليات الدفع"

    def __str__(self):
        return f"دفعة بمبلغ {self.amount} ريال"
