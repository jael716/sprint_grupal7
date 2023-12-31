# Generated by Django 4.2.3 on 2023-07-21 01:40

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
            name='Tarea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('descripcion', models.TextField()),
                ('creado_en', models.DateTimeField(auto_now_add=True)),
                ('estado', models.CharField(choices=[('P', 'Pendiente'), ('EP', 'En Progreso'), ('C', 'Completada')], default='P', max_length=2)),
                ('label', models.CharField(choices=[('T', 'Trabajo'), ('H', 'Hogar'), ('E', 'Estudio')], max_length=1)),
                ('asignado_a', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tareas', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
