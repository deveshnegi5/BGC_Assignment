# Generated by Django 3.0.6 on 2022-02-27 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20220227_1055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='Date_of_Purchase',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='Fuel',
            field=models.CharField(max_length=20),
        ),
    ]
