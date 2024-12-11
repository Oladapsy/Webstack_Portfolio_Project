from django.contrib import admin
from .models import UnifiedModel

@admin.register(UnifiedModel)
class UnifiedModelAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "invoice_number", "item_title", "quantity", "price", "due_date", "status")
    search_fields = ("name", "email", "invoice_number", "item_title")
    list_filter = ("due_date", "status")
    ordering = ("due_date",)