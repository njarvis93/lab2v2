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
            'nombre',
        ]
        labels = {
            'nombre': 'Medico',
        }
        widgets = {
            'nombre': forms.Select(attrs={'class':'form-control'}),
        }
