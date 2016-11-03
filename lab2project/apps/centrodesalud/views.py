from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView
from django.core.urlresolvers import reverse_lazy
from lab2project.apps.centrodesalud.models import *
from lab2project.apps.centrodesalud.forms import *
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

def index_view(request):

    ctx = {}
    return render(request, 'index.html',ctx)

def home_view(request):

    ctx = {}
    return render(request, 'examples/profile-page.html',ctx)

def nuevacita_view(request):
    ctx = {}
    return render(request, 'cita/cita.html', ctx)

def citas_view(request):
    ctx = []
    return render(request, 'cita/citas.html', ctx)


class CitaCreate(CreateView):
    model = Cita
    template_name = 'cita/cita.html'
    form_class = CitaForm
    second_form_class = PacienteForm
    tercer_form_class = EspecialidadForm
    cuarto_form_class = MedicoForm
    quinto_form_class = SucursalForm
    sexto_form_class = ClinicaForm
    fields = ['paciente', 'sucursal', 'medico', 'fecha', 'hora','descripcion_sintomas', 'tipo', 'estado']
    success_url = reverse_lazy('url_miscitas')

    def get_context_data(self, **kwargs):
        context = super(CitaCreate, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
        if 'form3' not in context:
            context['form3'] = self.tercer_form_class(self.request.GET)
        if 'form4' not in context:
            context['form4'] = self.cuarto_form_class(self.request.GET)
        if 'form5' not in context:
            context['form5'] = self.quinto_form_class(self.request.GET)
        if 'form6' not in context:
            context['form6'] = self.sexto_form_class(self.request.GET)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)
        form3 = self.tercer_form_class(request.POST)
        form4 = self.cuarto_form_class(request.POST)
        form5 = self.quinto_form_class(request.POST)
        form6 = self.sexto_form_class(request.POST)
        if form.is_valid() and form2.is_valid():
            cita = form.save(commit=False)
            cita.paciente = form2.save(commit=False)
            cita.medico.especialidad = form3.save(commit=False)
            cita.medico = form4.save(commit=False)
            clinica = form6.save(commit=False)
            cita.sucursal = form5.save(commit=False)
            cita.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form, form2=form2))

class CitaUpdate(UpdateView):
    model = Cita
    second_model = Paciente
    tercer_model = Especialidad
    cuarto_model = Medico
    quinto_model = Sucursal
    sexto_model = Clinica
    form_class = CitaForm
    second_form_class = PacienteForm
    tercer_form_class = EspecialidadForm
    cuarto_form_class = MedicoForm
    quinto_form_class = SucursalForm
    sexto_form_class = ClinicaForm
    template_name = 'cita/cita.html'
    fields = ['paciente', 'sucursal', 'medico', 'fecha', 'descripcion_sintomas', 'tipo']
    success_url = reverse_lazy('url_miscitas')

    def get_context_data(self, **kwargs):
        context = super(CitaUpdate, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk', 0)
        cita = self.model.objects.get(id=pk)
        paciente = self.second_model.objects.get(id=cita.paciente_id)
        medico = self.cuarto_model.objects.get(id=cita.medico_id)
        sucursal = self.quinto_model.objects.get(id=cita.sucursal_id)
        clinica = self.sexto_model.objects.get(id=sucursal.clinica_id)
        especialidad = self.tercer_model.objects.get(id=cita.medico_id)
        if 'form' not in context:
            context['form'] = self.form_class()
        if 'form2' not in context:
            context['form2'] = self.second_form_class(instance=paciente)
        if 'form3' not in context:
            context['form3'] = self.tercer_form_class(instance=especialidad)
        if 'form4' not in context:
            context['form4'] = self.cuarto_form_class(instance=medico)
        if 'form5' not in context:
            context['form5'] = self.quinto_form_class(instance=sucursal)
        if 'form6' not in context:
            context['form6'] = self.sexto_form_class(instance=clinica)
        context['id'] = pk
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        id_cita = kwargs['pk']
        cita = self.model.objects.get(id=id_cita)
        paciente = self.second_model.objects.get(id=cita.paciente_id)
        especialidad = self.tercer_model.objects.get(id=cita.medico_id)
        medico = self.cuarto_model.objects.get(id=cita.medico_id)
        sucursal = self.quinto_model.objects.get(id=cita.sucursal_id)
        clinica = self.sexto_model.objects.get(id=sucursal.clinica_id)
        form = self.form_class(request.POST, instance=cita)
        form2 = self.second_form_class(request.POST, instance=paciente)
        form3 = self.tercer_form_class(request.POST, instance=especialidad)
        form4 = self.cuarto_form_class(request.POST, instance=medico)
        form5 = self.quinto_form_class(request.POST, instance=sucursal)
        form6 = self.sexto_form_class(request.POST, instance=clinica)
        if form.is_valid() and form2.is_valid() and form3.is_valid() and form4.is_valid() and form5.is_valid() and form6.is_valid():
            form.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return HttpResponseRedirect(self.get_success_url())


class CitaListar(ListView):
    model = Cita
    template_name = 'cita/citas.html'
    paginate_by = 2

class CitaDelete(DeleteView):
    model = Cita
    success_url = reverse_lazy('url_miscitas')

class buscarPaciente3(DetailView):
    model = Paciente
    template_name = 'cita/cita.html'


class listas_especialidades(ListView):
    model = Especialidad
