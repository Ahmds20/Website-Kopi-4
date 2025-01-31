# Generated by Django 5.0.7 on 2024-11-14 07:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_cart_is_active_cartitem_is_active_alter_cart_user"),
        ("product", "0005_product_date_added"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="cart",
            name="is_active",
        ),
        migrations.AddField(
            model_name="cart",
            name="product",
            field=models.ForeignKey(
                default=7,
                on_delete=django.db.models.deletion.CASCADE,
                to="product.product",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="cart",
            name="quantity",
            field=models.PositiveIntegerField(default=1),
        ),
    ]
