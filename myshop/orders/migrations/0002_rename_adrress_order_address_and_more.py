# Generated by Django 5.0.1 on 2024-01-29 20:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='adrress',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='second_name',
            new_name='last_name',
        ),
    ]
