# Generated by Django 3.0.5 on 2020-06-23 00:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Avadell', '0010_auto_20200622_1839'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cotizacion',
            name='iva',
        ),
    ]
