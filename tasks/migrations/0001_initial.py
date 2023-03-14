# Generated by Django 4.1.6 on 2023-02-09 20:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bitacora',
            fields=[
                ('COD_bitacora', models.IntegerField(primary_key=True, serialize=False)),
                ('Horas_laboradas', models.IntegerField()),
                ('Fuentes_trabajados', models.CharField(max_length=70)),
                ('Tipo_fuente', models.CharField(max_length=70)),
                ('Descripcion', models.TextField(max_length=300)),
                ('Estado', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('Tipo_ID', models.CharField(max_length=10)),
                ('NID', models.IntegerField(primary_key=True, serialize=False)),
                ('Razon_social', models.CharField(max_length=70)),
                ('Direccion', models.CharField(max_length=70)),
                ('Email', models.CharField(max_length=70)),
                ('Telefono', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Ingeniero',
            fields=[
                ('COD_ingeniero', models.IntegerField(primary_key=True, serialize=False)),
                ('Identificacion', models.IntegerField()),
                ('Nombres', models.CharField(max_length=70)),
                ('Apellidos', models.CharField(max_length=70)),
                ('ROL', models.CharField(max_length=50)),
                ('Direccion', models.CharField(max_length=80)),
                ('Telefono', models.IntegerField()),
                ('Email', models.CharField(max_length=70)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('Codigo', models.IntegerField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=50)),
                ('Descripcion', models.TextField(max_length=500)),
                ('Costo', models.FloatField(max_length=(9, 2))),
                ('cliente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tasks.cliente')),
                ('ingeniero', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tasks.ingeniero')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Actividad',
            fields=[
                ('COD_actividad', models.IntegerField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=50)),
                ('Descripcion', models.TextField(max_length=500)),
                ('Costo', models.FloatField(max_length=(9, 2))),
                ('ingeniero', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tasks.ingeniero')),
                ('proyecto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tasks.proyecto')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]