# Generated by Django 2.2 on 2019-04-11 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0002_auto_20190411_0332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='es_privado',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='es_verificado',
            field=models.BooleanField(default=False),
        ),
    ]
