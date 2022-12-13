import datetime

from django.db import models

class Sales(models.Model):
    product_id = models.CharField(max_length=3)
    sold = models.IntegerField()
    income = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name_plural = 'Sales'


class DiscountSales(models.Model):
    product_id = models.CharField(max_length=3)
    sold = models.IntegerField()
    discount = models.IntegerField()
    income = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name_plural = 'Discount Sales'


class SalesWithoutDiscount(models.Model):
    product_id = models.CharField(max_length=3)
    sold = models.IntegerField()
    income = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name_plural = 'Sales Without Discount'

class OrderInfo(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    city = models.CharField(max_length=100)
    zip = models.IntegerField()
    phone_number = models.IntegerField()
    discount = models.IntegerField(blank=True)
    products = models.TextField(max_length=300)
    time = models.DateTimeField(auto_now=True)
    date = models.DateField(auto_now=True)
    delivery = models.BooleanField()

    class Meta:
        verbose_name_plural = 'Order Info'