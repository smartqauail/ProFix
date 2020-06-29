# Generated by Django 3.0.5 on 2020-06-22 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Avadell', '0009_auto_20200622_1836'),
    ]

    operations = [
        migrations.AddField(
            model_name='cotizacion',
            name='canti',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True, verbose_name='Cantidad item 1'),
        ),
        migrations.AddField(
            model_name='cotizacion',
            name='canti2',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Cantidad item 2'),
        ),
        migrations.AddField(
            model_name='cotizacion',
            name='canti3',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Cantidad item 3'),
        ),
        migrations.AddField(
            model_name='cotizacion',
            name='canti4',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Cantidad item 4'),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='cost',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True, verbose_name='Valor Unitario item 1'),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='cost2',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Valor Unitario item 2'),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='cost3',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Valor Unitario item 3'),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='cost4',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Valor Unitario item 4'),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='item2',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Descripción Item 2'),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='item3',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Descripción Item 3'),
        ),
        migrations.AlterField(
            model_name='cotizacion',
            name='item4',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Descripción Item 4'),
        ),
    ]
