from django.contrib import admin
from .models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category', 'available')
    list_display_links = ('name',)
    search_fields = ('name', 'id')
    list_editable = ('available',)


admin.site.register(Product, ProductAdmin)

admin.site.register(Category, CategoryAdmin)
