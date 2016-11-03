from django import forms
from lab2project.apps.centrodesalud.models import Cita, Paciente, Especialidad, Sucursal, Medico, Clinica

class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = [
            'fecha',
            'descripcion_sintomas',
            'tipo',
            'hora',
        ]
        labels = {
            'fecha': 'Fecha de la Cita',
            'descripcion_sintomas': 'Describa el motivo de su consulta',
            'tipo': 'Tipo de Cita',
            'hora': 'Hora de la Cita',
        }
        widgets={
            'fecha': forms.DateInput(attrs={'class':'form-control'}),
            'descripcion_sintomas': forms.Textarea(attrs={'class': 'form-control'}),
            'tipo': forms.RadioSelect(),
            'hora': forms.TimeInput(attrs={'class': 'form-control'}),
        }

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = [
            'cedula',
        ]

class EspecialidadForm(forms.ModelForm):
    class Meta:
        model = Especialidad
        fields = [
            'nombre',
        ]
        labels = {
            'nombre': 'Especialidad',
        }
        widgets = {
            'nombre': forms.Select(attrs={'class':'form-control'}),
        }

class SucursalForm(forms.ModelForm):
    class Meta:
        model = Sucursal
        fields = [
            'direccion',
            'telefono',

        ]
        labels = {
            'direccion': 'Dirección',
            'telefono': 'Telefono de contacto',
        }
        widgets = {
            'direccion': forms.Textarea(attrs={'class':'form-control'}),
            'telefono': forms.TextInput(attrs={'class':'form-control'}),

        }


class ClinicaForm(forms.ModelForm):
    class Meta:
        model = Clinica
        fields = [
            'nombre',
        ]
        labels = {
            'nombre': 'Nombre de la clinica',
        }
        widgets = {
            'nombre': forms.Select(attrs={'class': 'form-control'}),
        }


class MedicoForm(forms.ModelForm):
    class Meta:
        model = Medico
        fields = [
            'username',
            'nro_registro',
            'nombre',
            'apellido',
            'telefono',
            'direccion',
            'fecha_nacimiento',
            'especialidad',
            'clinica',
            'descripcion',
            'estudios',
            'email',
            'tipousuario',
        ]
        labels = {
            'username' : 'Nombre de Usuario',
            'nro_registro': 'Numero de su Registro Medico',
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'telefono': 'Telefono',
            'direccion': 'Direccion',
            'fecha_nacimiento': 'Fecha de nacimiento',
            'especialidad': 'Especialidades',
            'clinica': 'Clinicas',
            'descripcion': 'Descripcion',
            'estudios': 'Estudios',
            'email': 'Correo',
            'photo': 'Imagen',
            'tipousuario' : 'Tipo de usuario',
        }
        widgets = {
            'username': forms.Select(attrs={'class':'form-control'}),
            'nro_registro': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_nacimiento': forms.DateInput(attrs={'class': 'form-control'}),
            'especialidad': forms.CheckboxSelectMultiple(),
            'clinica': forms.CheckboxSelectMultiple(),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'estudios': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'photo': forms.ClearableFileInput(), # ClearableFileInput
            'tipousuario' : forms.CheckboxChoiceInput(),
        }
