# Generated by Django 4.1.1 on 2022-12-07 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShopAdmin', '0005_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='delivery_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
