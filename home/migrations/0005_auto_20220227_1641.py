# Generated by Django 3.0.6 on 2022-02-27 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20220227_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='Date_of_Purchase',
            field=models.TextField(),
        ),
    ]
