from django.db import models

class Account(models.Model):
    """يمثل المستخدم داخل النظام (مستقبلاً يمكن ربطه بنظام المستخدمين الأصلي)."""

    name = models.CharField(
        max_length=100,
        verbose_name="الاسم الكامل"
    )

    email = models.EmailField(
        unique=True,
        verbose_name="البريد الإلكتروني"
    )

    date_joined = models.DateTimeField(
        auto_now_add=True,
        verbose_name="تاريخ الانضمام"
    )

    class Meta:
        verbose_name = "حساب مستخدم"
        verbose_name_plural = "حسابات المستخدمين"

    def __str__(self):
        return self.name
