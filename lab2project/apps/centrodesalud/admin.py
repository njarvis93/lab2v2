from django.contrib import admin
from .models import *
# Register your models here.}

#from models import *
from django.contrib import admin
from .models import *
from django.contrib.auth.models import Permission
from django.contrib.auth.admin import UserAdmin, UserChangeForm, UserCreationForm, AdminPasswordChangeForm
from django import forms
from django.utils.translation import ugettext_lazy as _

# from constance.admin import Config

from django.contrib import admin

class UsuarioChangeForm(UserChangeForm):
    class Meta:
        model = Usuario
        fields = '__all__'

    pass



class UsuarioCreationForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ('cedula', 'email', 'password1', 'password2')

    pass


class UsuarioAdmin(UserAdmin):
    list_display = (
    'cedula', 'nombres', 'apellidos', 'email', 'is_staff', 'is_superuser')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('cedula', 'username', 'nombres', 'apellidos', 'fecha_nacimiento',
        'email','telefono', 'sexo', 'imagen_perfil')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        (_('Datos'), {'fields': (
        'direccion', 'ocupacion',)}),

    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('cedula', 'username', 'email', 'password1', 'password2'),
        }),
    )
    form = UserChangeForm
    add_form = UsuarioCreationForm
    change_password_form = AdminPasswordChangeForm
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('username', 'cedula', 'nombres', 'apellidos', 'email')
    ordering = ('username',)
    filter_horizontal = ('groups', 'user_permissions',)
    pass



admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Clinica)
admin.site.register(Sucursal)
admin.site.register(Cita)