# Generated by Django 4.1.1 on 2022-10-12 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShopAdmin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='desc',
            field=models.CharField(blank=True, default='', max_length=5000, null=True),
        ),
    ]