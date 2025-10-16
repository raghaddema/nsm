# دور هذا الملف توجيه عمل النظام كاملا
from django.contrib import admin
from django.urls import path, include  # ← لإضافة روابط التطبيقات

urlpatterns = [
    # لوحة التحكم
    path("admin/", admin.site.urls),

    # روابط التطبيقات الثلاثة
    path("accounts/", include("accounts.urls")),
    path("shop/", include("shop.urls")),
    path("payments/", include("payments.urls")),
]
