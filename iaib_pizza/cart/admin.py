from django.contrib import admin
from .models import Sales, DiscountSales, SalesWithoutDiscount, OrderInfo

class SalesAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'sold', 'income')
    list_display_links = ('product_id',)
    search_fields = ('id',)


class DiscountSalesAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'sold', 'discount', 'income')
    list_display_links = ('product_id',)
    search_fields = ('id', 'discount')


class SalesWithoutDiscountAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'sold', 'income')
    list_display_links = ('product_id',)
    search_fields = ('id',)


class OrderInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'city', 'zip', 'phone_number', 'discount', 'products', 'amount', 'time', 'date')
    search_fields = ('name', 'city', 'zip', 'phone_number', 'discount', 'products')


admin.site.register(Sales, SalesAdmin)
admin.site.register(SalesWithoutDiscount, SalesWithoutDiscountAdmin)
admin.site.register(DiscountSales, DiscountSalesAdmin)
admin.site.register(OrderInfo, OrderInfoAdmin)
