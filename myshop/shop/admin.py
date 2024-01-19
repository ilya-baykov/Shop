from django.contrib import admin

# Register your models here.
from .models import Product, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['category', 'slug', 'name', 'descriprtion', 'image', 'price', 'available', 'created', 'updated']
    list_filter = ['price', 'name', 'created', 'updated']
    list_display_links = ["slug", 'name']
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ['price', 'available']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ['name', 'slug']
    list_filter = ['name']
    search_fields = ['name']
