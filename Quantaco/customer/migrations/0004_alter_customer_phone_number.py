# Generated by Django 4.0.10 on 2024-05-18 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_alter_customer_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phone_number',
            field=models.CharField(default='', max_length=13),
        ),
    ]
