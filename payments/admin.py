from django.contrib import admin
from .models import Payment

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    """عرض نموذج الدفع داخل لوحة التحكم"""
    list_display = ("amount", "method", "payment_date")
    list_filter = ("method", "payment_date")
    ordering = ("-payment_date",)
