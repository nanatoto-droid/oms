from django.contrib import admin
from .models import Product, Category, Tag

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'sku', 'category', 'stock', 'is_active', 'created_at')
    list_filter = ('is_active', 'category', 'tags')
    search_fields = ('name', 'sku', 'description')   # required for autocomplete
    autocomplete_fields = ('category', 'tags')       # only FK or M2M allowed

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('name', 'slug')

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ('name',)