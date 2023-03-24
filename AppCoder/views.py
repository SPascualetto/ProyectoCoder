from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Profesores, Alumnos, Egresados, Institucional, Comentario
from AppCoder.forms import FormularioRegistroUsuario, FormularioEdicion, FormularioPassCambio
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views.generic import TemplateView, ListView, DetailView, UpdateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView 
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse_lazy

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'inicio.html'

class Login(LoginView):
    template_name = 'login.html'
    fields = '__all__'
    redirect_autheticated_user = True
    success_url = reverse_lazy('inicio')

    def get_success_url(self):
        return reverse_lazy('inicio')

class Registro(FormView):
    template_name = 'registro.html'
    form_class = FormularioRegistroUsuario
    redirect_autheticated_user = True
    success_url = reverse_lazy('inicio')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(Registro, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('inicio')
        return super(Registro, self).get(*args, **kwargs)

class UsuarioEditar(UpdateView):
    form_class = FormularioEdicion
    template_name= 'Usuarioeditar.html'
    success_url = reverse_lazy('inicio')

    def get_object(self):
        return self.request.user
    
class PassCambio(PasswordChangeView):
    form_class = FormularioPassCambio
    template_name = 'passCambio.html'
    success_url = reverse_lazy('passOk')

def PassOK(request):
    return render(request, 'passOk.html', {})
     
            
#Profesores

class ProfesoresLista(LoginRequiredMixin, ListView):
    context_object_name = 'profesores'
    queryset = Profesores.objects.filter(apellido__startswith='profesores')
    template_name = 'profesoresLista.html'
    login_url = '/login/'

class ProfesoresDetalle(LoginRequiredMixin, DetailView):
    model = Profesores
    context_object_name = 'profesores'
    template_name = 'profesoresDetalle.html'

class ProfesoresUpdate(LoginRequiredMixin, UpdateView):
    model = Profesores
    success_url = reverse_lazy('profesores')
    context_object_name = 'profesores'
    template_name = 'profesoresUpdate.html'

class ProfesoresDelete(LoginRequiredMixin, DeleteView):
    model = Profesores
    success_url = reverse_lazy('profesores')
    context_object_name = 'profesores'
    template_name = 'profesoresEliminar.html'


#Alumnos
class AlumnosLista(LoginRequiredMixin, ListView):
    context_object_name = 'alumnos'
    queryset = Alumnos.objects.filter(apellido__startswith='alumnos')
    template_name = 'alumnosLista.html'
    login_url = '/login/'

class AlumnosDetalle(LoginRequiredMixin, DetailView):
    model = Alumnos
    context_object_name = 'alumnos'
    template_name = 'alumnosDetalle.html'

class AlumnosUpdate(LoginRequiredMixin, UpdateView):
    model = Alumnos
    success_url = reverse_lazy('alumnos')
    context_object_name = 'alumnos'
    template_name = 'alumnosUpdate.html'

class AlumnosDelete(LoginRequiredMixin, DeleteView):
    model = Alumnos
    success_url = reverse_lazy('alumnos')
    context_object_name = 'alumnos'
    template_name = 'alumnosDelete.html'

#Egresados
class EgresadosLista(LoginRequiredMixin, ListView):
    context_object_name = 'egresados'
    queryset = Egresados.objects.filter(apellido__startswith='egresados')
    template_name = 'egresadosLista.html'
    login_url = '/login/'

class EgresadosDetalle(LoginRequiredMixin, DetailView):
    model = Egresados
    context_object_name = 'egresados'
    template_name = 'egresadosDetalle.html'

class EgresadosUpdate(LoginRequiredMixin, UpdateView):
    model = Egresados
    success_url = reverse_lazy('egresados')
    context_object_name = 'egresados'
    template_name = 'egresadosUpdate.html'

class EgresadosDelete(LoginRequiredMixin, DeleteView):
    model = Egresados
    success_url = reverse_lazy('egresados')
    context_object_name = 'egresados'
    template_name = 'egresadosDelete.html'


#Institucional
class InstitucionalLista(LoginRequiredMixin, ListView):
    context_object_name = 'institucional'
    queryset = Institucional.objects.filter(apellido__startswith='institucional')
    template_name = 'institucionalLista.html'
    login_url = '/login/'

class InstitucionalDetalle(LoginRequiredMixin, DetailView):
    model = Institucional
    context_object_name = 'institucional'
    template_name = 'institucionalDetalle.html'

class InstitucionalUpdate(LoginRequiredMixin, UpdateView):
    model = Institucional
    success_url = reverse_lazy('institucional')
    context_object_name = 'institucional'
    template_name = 'institucionalUpdate.html'

class InstitucionalDelete(LoginRequiredMixin, DeleteView):
    model = Institucional
    success_url = reverse_lazy('institucional')
    context_object_name = 'institucional'
    template_name = 'institucionalDelete.html'

#Busqueda
def buscarpadron(request):
    return render(request, 'buscarpadron.html')

def buscar(request):
    if request.GET['padron']:
        padron = request.GET['padron']
        alumno = Alumnos.objects.filter(padron__icontains=padron)
        return render(request, 'resultadosBusqueda.html', {"alumno": alumno, "padron": padron})
    else:
        respuesta ="No enviaste datos"
        return HttpResponse(respuesta)
