from django.shortcuts import render, render_to_response
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


    success_url = reverse_lazy('url_miscitas')

    def get_context_data(self, **kwargs):
        context = super(CitaCreate, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)

        if form.is_valid() and form2.is_valid():
            cita = form.save(commit=False)
            cita.paciente = form2.save(commit=False)
            cita.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form, form2=form2))

class CitaUpdate(UpdateView):
    model = Cita
    second_model = Paciente
    form_class = CitaForm
    second_form_class = PacienteForm

    template_name = 'cita/cita.html'

    success_url = reverse_lazy('url_miscitas')

    def get_context_data(self, **kwargs):
        context = super(CitaUpdate, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk', 0)
        cita = self.model.objects.get(id=pk)
        paciente = self.second_model.objects.get(cedula=cita.paciente_id)

        if 'form' not in context:
            context['form'] = self.form_class()
        if 'form2' not in context:
            context['form2'] = self.second_form_class(instance=paciente)

        context['id'] = pk
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        id_cita = kwargs['pk']
        cita = self.model.objects.get(id=id_cita)
        paciente = self.second_model.objects.get(cedula=cita.paciente_id)

        form = self.form_class(request.POST, instance=cita)
        form2 = self.second_form_class(request.POST, instance=paciente)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return render_to_response('cita/error.html', {'form': form})



class CitaListar(ListView):
    model = Cita
    template_name = 'cita/citas.html'
    paginate_by = 5

class CitaDelete(DeleteView):
    model = Cita
    template_name = 'cita/cita_confirm_delete.html'
    success_url = reverse_lazy('url_miscitas')

class buscarPaciente3(DetailView):
    model = Paciente
    template_name = 'cita/cita.html'


class listas_especialidades(ListView):
    model = Especialidad

def get_especialidad():
    especialidades = ()
    for especialidad in Especialidad.objects.all():
        especialidades.__add__(especialidad.pk, especialidad.nombre)
    return especialidades