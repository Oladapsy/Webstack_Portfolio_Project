from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Client, Invoice, Item

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("company_name", "email") # fields to show in the admin list view
    search_fields = ("company_name", "email") # enable searching by name or email
    odering = ("company_name") # order alphabetically by name

@admin.register(Invoice)
class InvoiceAsmin(admin.ModelAdmin):
    list_display = ("invoice_number", "client", "total_amount", "due_date", "status")
    search_fields = ("invoice_number", "client__company_name")
    list_filter = ("due_date",)
    ordering = ("due_date",)

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "quantity", "price", "invoice")
    search_fields = ("title", "invoice__invoice_number")
    list_filter = ("invoice",)