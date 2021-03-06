# Generated by Django 4.0.2 on 2022-02-18 01:54

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_orderdetail_order_alter_orderdetail_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdetail',
            name='cuantity',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='orderdetail',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.product'),
        ),
    ]
