# Generated by Django 4.1.3 on 2022-12-14 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_rename_quantity_orderinfo_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderinfo',
            name='amount',
            field=models.TextField(max_length=300),
        ),
    ]