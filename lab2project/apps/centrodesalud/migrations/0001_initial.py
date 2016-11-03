# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-03 20:06
from __future__ import unicode_literals

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.datetime_safe
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(max_length=20, verbose_name='username')),
                ('nombres', models.CharField(max_length=254, verbose_name='Nombres')),
                ('apellidos', models.CharField(max_length=300, verbose_name='Apellidos')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email')),
                ('direccion', models.TextField(verbose_name='Direccion')),
                ('fecha_nacimiento', models.DateField(default=django.utils.datetime_safe.datetime.now, verbose_name='Fecha de Nacimiento')),
                ('ocupacion', models.TextField(verbose_name='Ocupacion')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='is active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('telefono', models.CharField(max_length=20, null=True)),
                ('cedula', models.CharField(max_length=20, unique=True, verbose_name='Cedula')),
                ('sexo', models.CharField(max_length=20, verbose_name='Sexo')),
                ('imagen_perfil', models.ImageField(blank=True, null=True, upload_to='img/perfil/usuario/', verbose_name='Imagen de Perfil')),
                ('tipo_usuario', models.CharField(max_length=20, verbose_name='Tipo de usuario')),
                ('descripcion', models.TextField(blank=True, max_length=300, null=True, verbose_name='Descripciones')),
                ('nro_registro', models.CharField(blank=True, max_length=10, null=True, verbose_name='Nro de Registro')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='AntecedenteClinico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField(max_length=100)),
                ('fecha_registro', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='AntecedenteFamiliar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField(max_length=100)),
                ('fecha_aproximada', models.DateField()),
                ('parentesco', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Cita',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
                ('descripcion_sintomas', models.TextField(blank=True, null=True)),
                ('tipo', models.IntegerField()),
                ('estado', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Clinica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('tipo', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CuadroClinico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField(max_length=50)),
                ('nombre_formal', models.CharField(max_length=20)),
                ('nombre_comun', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Enfermedad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('nombre_cientifico', models.CharField(max_length=20)),
                ('epidemiologia', models.CharField(max_length=30)),
                ('duracion', models.CharField(max_length=10)),
                ('distribucion', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Especialidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('area', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='HistoriaClinica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ante_clinicos', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='centrodesalud.AntecedenteClinico')),
                ('ante_familiares', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='centrodesalud.AntecedenteFamiliar')),
            ],
        ),
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('hora_inicio', models.DateTimeField()),
                ('hora_fin', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Medicamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_comun', models.CharField(max_length=20)),
                ('nombre_cientifico', models.CharField(max_length=30)),
                ('principios_activos', models.TextField(max_length=100)),
                ('efectos_secundarios', models.TextField(max_length=100)),
                ('indicaciones', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('nro_registro', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=20)),
                ('telefono', models.CharField(max_length=12)),
                ('direccion', models.TextField(max_length=50)),
                ('fecha_nacimiento', models.DateField()),
                ('clinica', models.ManyToManyField(to='centrodesalud.Clinica')),
                ('especialidad', models.ManyToManyField(to='centrodesalud.Especialidad')),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('cedula', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('fecha_nacimiento', models.DateField()),
                ('telefono', models.CharField(max_length=12)),
                ('peso', models.IntegerField()),
                ('estatura', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='RegistrarUsuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('contrasenna', models.TextField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion', models.TextField(max_length=50)),
                ('telefono', models.CharField(max_length=12)),
                ('director', models.CharField(blank=True, max_length=20)),
                ('clinica', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='centrodesalud.Clinica')),
            ],
        ),
        migrations.CreateModel(
            name='Tratamiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duracion', models.TextField()),
                ('tipo', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='horario',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='centrodesalud.Medico'),
        ),
        migrations.AddField(
            model_name='historiaclinica',
            name='paciente',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='centrodesalud.Paciente'),
        ),
        migrations.AddField(
            model_name='cita',
            name='medico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='centrodesalud.Medico'),
        ),
        migrations.AddField(
            model_name='cita',
            name='paciente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='centrodesalud.Paciente'),
        ),
        migrations.AddField(
            model_name='cita',
            name='sucursal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='centrodesalud.Sucursal'),
        ),
        migrations.AddField(
            model_name='antecedentefamiliar',
            name='tratamiento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='centrodesalud.Tratamiento'),
        ),
        migrations.AddField(
            model_name='antecedenteclinico',
            name='medico_tratante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='centrodesalud.Medico'),
        ),
        migrations.AddField(
            model_name='antecedenteclinico',
            name='tratamiento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='centrodesalud.Tratamiento'),
        ),
    ]
