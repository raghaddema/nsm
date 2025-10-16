from django.db import models

class Account(models.Model):
    """يمثل المستخدم داخل النظام (مستقبلاً يمكن ربطه بـ User الأصلي)."""
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Account"
        verbose_name_plural = "Accounts"

    def __str__(self):
        return self.name
