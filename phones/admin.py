from django.contrib import admin
from .models import Category, Product, CustomUser

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}  # Автозаполнение поля slug на основе name

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'category', 'price', 'in_stock')
    prepopulated_fields = {'slug': ('name',)}  # Автозаполнение поля slug на основе name

@admin.register(CustomUser )
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')
