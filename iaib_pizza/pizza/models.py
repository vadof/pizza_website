from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    ingredients = models.TextField(max_length=500, blank=True, null=True)
    ml = models.SmallIntegerField(blank=True, null=True)
    image = models.ImageField(upload_to="product_images/")
    available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name
