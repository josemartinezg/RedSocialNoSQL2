# Generated by Django 2.2 on 2019-04-11 06:08

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('publicacion', '0001_initial'),
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.CharField(max_length=200)),
                ('fecha_publicado', models.DateField(default=datetime.datetime.now)),
                ('id_perfil', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='usuario.Usuario')),
                ('id_publicacion', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='publicacion.Publicacion')),
            ],
        ),
    ]
