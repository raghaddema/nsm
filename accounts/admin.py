from django.contrib import admin
from .models import Account

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    """عرض نموذج المستخدم داخل لوحة التحكم"""
    list_display = ("name", "email", "date_joined")
    search_fields = ("name", "email")
    ordering = ("-date_joined",)
