from django import forms
from lab2project.apps.centrodesalud.models import Cita, Paciente, Especialidad, Sucursal, Medico, Clinica
from lab2project.apps.centrodesalud import views

class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = [
            'fecha',
            'descripcion_sintomas',
            'tipo',
            'hora',
            'especialidad',
            'medico',
            'sucursal',
        ]
        labels = {
            'fecha': 'Fecha de la Cita',
            'descripcion_sintomas': 'Describa el motivo de su consulta',
            'tipo': 'Tipo de Cita',
            'hora': 'Hora de la Cita',
            'especialidad': 'Especialidad',
            'medico': 'Medico Tratante',
            'sucursal': 'Clinica',
        }
        widgets={
            'fecha': forms.DateInput(attrs={'class': 'datepicker form-control'}),
            'descripcion_sintomas': forms.Textarea(attrs={'class': 'form-control', 'rows': '2'}),
            'tipo': forms.Select(attrs={'class': 'form-control'}, choices=model.tipos),
            'hora': forms.TimeInput(attrs={'class': 'form-control'}),
            'especialidad': forms.Select(attrs={'class': 'form-control'}),
            'medico': forms.Select(attrs={'class': 'form-control'}),
            'sucursal': forms.Select(attrs={'class': 'form-control'}),

        }

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = [
            'cedula',
        ]


