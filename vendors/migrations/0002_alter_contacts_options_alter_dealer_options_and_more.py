# Generated by Django 5.0.1 on 2024-01-25 12:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contacts',
            options={'verbose_name': 'contacts', 'verbose_name_plural': 'contacts'},
        ),
        migrations.AlterModelOptions(
            name='dealer',
            options={'verbose_name': 'dealer', 'verbose_name_plural': 'dealers'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'product', 'verbose_name_plural': 'products'},
        ),
    ]