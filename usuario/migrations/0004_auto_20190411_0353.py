# Generated by Django 2.2 on 2019-04-11 07:53

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0003_auto_20190411_0333'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='ciudad',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AddField(
            model_name='usuario',
            name='linea_direccion_1',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AddField(
            model_name='usuario',
            name='linea_direccion_2',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AddField(
            model_name='usuario',
            name='pais_residente',
            field=django_countries.fields.CountryField(blank=True, max_length=2),
        ),
        migrations.AddField(
            model_name='usuario',
            name='sector',
            field=models.CharField(blank=True, max_length=120),
        ),
    ]
