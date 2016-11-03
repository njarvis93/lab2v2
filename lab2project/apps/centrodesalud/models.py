from django.db import models
# -*- encoding: utf-8 -*-
# -*- coding: utf-8 -*-

import random
import string
from django.db import models
from django.db.models.fields import BooleanField
from datetime import datetime
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin,
                                        UserManager, Permission, Group)
from django.contrib.auth.models import User
from django.utils.datetime_safe import datetime
from datetime import datetime, date, timedelta
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.core.mail import EmailMultiAlternatives
from django.db import models
from datetime import *
from django.template import Context
from django.template.defaultfilters import date as _date
from django.template.loader import get_template
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from django.utils.datetime_safe import datetime


class Usuario(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=20, verbose_name=_('username'))
    nombres = models.CharField(_('Nombres'), max_length=254)
    apellidos = models.CharField(_('Apellidos'), max_length=300)
    email = models.EmailField(_('email'), max_length=254, unique=True)
    direccion = models.TextField(verbose_name=_('Direccion'))
    fecha_nacimiento = models.DateField(verbose_name=_('Fecha de Nacimiento'), default=datetime.now, null=False,
                                        blank=False)
    ocupacion = models.TextField(verbose_name=_('Ocupacion'))
    is_staff = models.BooleanField(_('staff status'), default=False,
                                   help_text=_('Designates whether the user can log into this admin '
                                               'site.'))
    is_active = models.BooleanField(_('is active'), default=True,
                                    help_text=_('Designates whether this user should be treated as '
                                                'active. Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    telefono = models.CharField(null=True, max_length=20)
    cedula = models.CharField(verbose_name=_('Cedula'), max_length=20, unique=True)
    sexo = models.CharField(verbose_name=_('Sexo'), max_length=20)
    imagen_perfil = models.ImageField(blank=True, null=True, upload_to='img/perfil/usuario/',
                                      verbose_name=_('Imagen de Perfil'))
    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'cedula', 'fecha_nacimiento', 'nombres', 'apellidos']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __unicode__(self):
        return self.get_full_name() + ('_') + self.cedula

    def get_absolute_url(self):
        return "/perfil/usuario/%d/" % self.id

    def get_full_name(self):
        """
        Retorna el nombre  completo del usuario
        """
        return self.nombres + ' ' + self.apellidos

    def get_short_name(self):
        """ Retorna el nombre corto del usuario """
        return self.cedula

        # Metodo de envio de template

    def new_password(self, password):
        self.set_password(password)
        self.password_is_auto = False
        self.save()

    def __str__(self):
        return '%s' % (self.cedula) + '_' + (self.get_full_name())


class Clinica(models.Model):
    nombre = models.CharField(max_length=50)
    tipo = models.IntegerField()  # 1=Public 0=Private


class Sucursal(models.Model):
    direccion = models.TextField(max_length=50)
    telefono = models.CharField(max_length=12)
    director = models.CharField(max_length=20, blank=True)
    clinica = models.ForeignKey(Clinica, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % (self.clinica.nombre)


class Tratamiento(models.Model):
    duracion = models.TextField()
    tipo = models.CharField(max_length=30)


# Create your models here.
class Especialidad(models.Model):
    nombre = models.CharField(max_length=20)
    area = models.CharField(max_length=20)


class Medico(models.Model):
    nro_registro = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    telefono = models.CharField(max_length=12)
    direccion = models.TextField(max_length=50)
    fecha_nacimiento = models.DateField()
    especialidad = models.ManyToManyField(Especialidad)
    clinica = models.ManyToManyField(Clinica)

    def __str__(self):
        return '%s' % (self.nombre)


class Paciente(models.Model):
    cedula = models.CharField(max_length=12, primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    telefono = models.CharField(max_length=12)
    peso = models.IntegerField()
    estatura = models.IntegerField()

    def __str__(self):
        return '%s' % (self.nombre)


# Create your models here.
class Cita(models.Model):
    medico = models.ForeignKey(Medico, null=False, blank=False, on_delete=models.CASCADE)
    sucursal = models.ForeignKey(Sucursal, null=False, blank=False, on_delete=models.CASCADE)
    paciente = models.ForeignKey(Paciente, null=False, blank=False, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    descripcion_sintomas = models.TextField(null=True, blank=True)
    tipo = models.IntegerField(null=False, blank=False)  # 1. Consulta 2. Entrega de Resultados
    estado = models.CharField(max_length=20) # 1=Programada, 2=Cancelada, 3=En Progreso

    def get_absolute_url(self):
        return reverse('url_miscitas')

    def get_tipo_cita(self):
        if self.tipo == 1:
            return 'Consulta'
        else:
            return 'Entrega de Examenes'

    def get_estado(self):
        estados = {'1': 'Programada', '2': 'Cancelada', '3': 'En progreso'}
        return estados[self.estado]


# Create your models here.
class Enfermedad(models.Model):
    nombre = models.CharField(max_length=20)
    nombre_cientifico = models.CharField(max_length=20)
    epidemiologia = models.CharField(max_length=30)
    duracion = models.CharField(max_length=10)
    distribucion = models.CharField(max_length=20)


class CuadroClinico(models.Model):
    descripcion = models.TextField(max_length=50)
    nombre_formal = models.CharField(max_length=20)
    nombre_comun = models.CharField(max_length=20)


class AntecedenteFamiliar(models.Model):
    descripcion = models.TextField(max_length=100)
    fecha_aproximada = models.DateField()
    parentesco = models.CharField(max_length=20)
    tratamiento = models.ForeignKey(Tratamiento, null=True, blank=True, on_delete=models.CASCADE)


class AntecedenteClinico(models.Model):
    descripcion = models.TextField(max_length=100)
    fecha_registro = models.DateField()
    tratamiento = models.ForeignKey(Tratamiento, null=True, blank=True, on_delete=models.CASCADE)
    medico_tratante = models.ForeignKey(Medico, null=False, blank=False, on_delete=models.CASCADE)


class HistoriaClinica(models.Model):
    paciente = models.OneToOneField(Paciente, on_delete=models.CASCADE)
    ante_familiares = models.ForeignKey(AntecedenteFamiliar, null=False, blank=False, on_delete=models.CASCADE)
    ante_clinicos = models.ForeignKey(AntecedenteClinico, null=True, blank=False, on_delete=models.CASCADE)


class Horario(models.Model):
    fecha = models.DateField()
    hora_inicio = models.DateTimeField(auto_now=False, auto_now_add=False)
    hora_fin = models.DateTimeField(auto_now=False, auto_now_add=False)
    doctor = models.ForeignKey(Medico, null=False, blank=False, on_delete=models.CASCADE)


class Medicamento(models.Model):
    nombre_comun = models.CharField(max_length=20)
    nombre_cientifico = models.CharField(max_length=30)
    principios_activos = models.TextField(max_length=100)
    efectos_secundarios = models.TextField(max_length=100)
    indicaciones = models.TextField(max_length=200)


class RegistrarUsuario(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    contrasenna = models.TextField(max_length=10)
