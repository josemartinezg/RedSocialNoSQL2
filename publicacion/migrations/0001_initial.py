# Generated by Django 2.2 on 2019-04-11 05:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publicacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=200)),
                ('fecha_publicado', models.DateField()),
                ('hora_publicado', models.DateTimeField()),
                ('id_perfil', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='usuario.Usuario')),
            ],
        ),
    ]
