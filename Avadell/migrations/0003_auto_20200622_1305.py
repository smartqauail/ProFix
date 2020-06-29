# Generated by Django 3.0.5 on 2020-06-22 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Avadell', '0002_proyectosavadell'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='porcet',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True, verbose_name='Porcetanje de Anticipo %'),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='porcet2',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True, verbose_name='Avance de Obra %'),
        ),
    ]
