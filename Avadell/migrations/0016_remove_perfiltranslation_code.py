# Generated by Django 3.0.5 on 2020-06-24 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Avadell', '0015_auto_20200624_1051'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfiltranslation',
            name='code',
        ),
    ]
