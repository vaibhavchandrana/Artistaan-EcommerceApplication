# Generated by Django 4.1.1 on 2022-09-10 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('img1', models.ImageField(upload_to='products/')),
                ('img2', models.ImageField(upload_to='products/')),
                ('img3', models.ImageField(upload_to='products/')),
                ('prod_category', models.CharField(max_length=50)),
            ],
        ),
    ]
