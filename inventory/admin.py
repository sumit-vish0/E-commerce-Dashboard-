from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "category", "price", "quantity", "supplier", "added_date")
    list_filter = ("category",)
    search_fields = ("name", "supplier")
