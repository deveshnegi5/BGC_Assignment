# Generated by Django 3.0.6 on 2022-02-28 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20220228_1234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='Customer_Marital_status',
            field=models.BooleanField(default=False),
        ),
    ]