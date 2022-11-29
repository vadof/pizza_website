from django.contrib import admin
from .models import Pizza, Burger, Drink, Category


class Pizza_Burger_Admin(admin.ModelAdmin):
    list_display = ('name', 'price', 'ingredients', 'available')
    list_display_links = ('name',)
    search_fields = ('name',)
    list_editable = ('available',)


class Drink_Admin(admin.ModelAdmin):
    list_display = ('name', 'price', 'ml', 'available')
    list_display_links = ('name',)
    search_fields = ('name',)
    list_editable = ('available',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')


admin.site.register(Pizza, Pizza_Burger_Admin)
admin.site.register(Burger, Pizza_Burger_Admin)
admin.site.register(Drink, Drink_Admin)

admin.site.register(Category, CategoryAdmin)
