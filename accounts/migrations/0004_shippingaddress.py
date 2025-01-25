# Generated by Django 5.1.4 on 2025-01-19 11:13

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_shopper_managers'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShippingAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=242)),
                ('address_1', models.CharField(help_text='Street address and number.', max_length=1024)),
                ('address_2', models.CharField(blank=True, help_text=' Hall, floor, place name...', max_length=1024)),
                ('city', models.CharField(max_length=1024)),
                ('zip_code', models.CharField(max_length=33)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
