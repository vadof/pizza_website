import datetime

from django.db import models

class Sales(models.Model):
    product_id = models.IntegerField()
    sold = models.IntegerField()
    income = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name_plural = 'Sales'
        ordering = ['product_id']


class DiscountSales(models.Model):
    product_id = models.IntegerField()
    sold = models.IntegerField()
    discount = models.IntegerField()
    income = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name_plural = 'Discount Sales'
        ordering = ['product_id', 'discount']


class SalesWithoutDiscount(models.Model):
    product_id = models.IntegerField()
    sold = models.IntegerField()
    income = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name_plural = 'Sales Without Discount'
        ordering = ['product_id']

class OrderInfo(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    city = models.CharField(max_length=100)
    zip = models.IntegerField()
    phone_number = models.IntegerField()
    discount = models.IntegerField(blank=True, null=True)
    products = models.TextField(max_length=300)
    amount = models.TextField(max_length=300)
    time = models.TimeField(auto_now_add=True)
    date = models.DateField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Order Info'