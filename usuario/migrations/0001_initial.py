# Generated by Django 2.2 on 2019-04-11 05:12

import datetime
from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('apellido', models.CharField(max_length=200)),
                ('nombre_usuario', models.CharField(max_length=200)),
                ('correo_electronico', models.EmailField(max_length=200)),
                ('fecha_nacimiento', models.DateField()),
                ('sexo', models.CharField(max_length=2)),
                ('descripcion', models.TextField(blank=True)),
                ('pais_nacimiento', django_countries.fields.CountryField(max_length=2)),
                ('telefono', models.CharField(max_length=20)),
                ('es_verificado', models.BooleanField(default=False)),
                ('es_privado', models.BooleanField(default=False)),
                ('foto_perfil', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('coordenadas', models.CharField(max_length=200)),
                ('hire_datte', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
