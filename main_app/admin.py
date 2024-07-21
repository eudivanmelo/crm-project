from typing import Any
from django.contrib import admin
from .models import Category, Product, StockItem

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_by', 'updated_at')
    search_fields = ('name', 'created_by')
    list_filter = ('created_at', 'updated_at', 'name', 'created_by')
    exclude = ['created_by']

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.created_by = request.user

        return super().save_model(request, obj, form, change)
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'value', 'category', 'created_at', 'updated_at', 'created_by')
    search_fields = ('name', 'description', 'category__name')
    list_filter = ('created_at', 'updated_at', 'category')
    exclude = ['created_by']

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.created_by = request.user
        super().save_model(request, obj, form, change)

@admin.register(StockItem)
class StockItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'barcode', 'quantity', 'manufacture_date', 'expiration_date', 'created_by')
    search_fields = ('product__name', 'barcode')
    list_filter = ('product', 'expiration_date', 'created_by')
    exclude = ['created_by']

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.created_by = request.user
        super().save_model(request, obj, form, change)