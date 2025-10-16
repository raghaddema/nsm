from django.db import models


class Product(models.Model):
    """نموذج يمثل منتجًا في المتجر."""

    name = models.CharField(
        max_length=150,
        verbose_name="اسم المنتج"
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="السعر (ريال)"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="تاريخ الإضافة"
    )

    class Meta:
        verbose_name = "منتج"
        verbose_name_plural = "المنتجات"

    def __str__(self):
        return self.name
