# Generated by Django 5.0.7 on 2024-08-02 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffee_house_app', '0002_alter_cakes_price_alter_coffees_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cakes',
            name='price',
            field=models.IntegerField(max_length=10),
        ),
        migrations.AlterField(
            model_name='coffees',
            name='price',
            field=models.IntegerField(max_length=10),
        ),
    ]