# Generated by Django 4.1.1 on 2022-10-13 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShopAdmin', '0004_remove_admin_pan'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(blank=True, default='', max_length=30),
        ),
    ]
