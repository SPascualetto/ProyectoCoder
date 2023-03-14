from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Profesores, Alumnos, Egresados, Institucional
from AppCoder.forms import ProfesoresFormulario, AlumnosFormulario, EgresadosFormulario, InstitucionalFormulario

def inicio(request):
    return render(request, "inicio.html")

#Profesores
def profesores(request):
    return render(request, "profesores.html")

def profesoresformulario (request):
    if request.method == 'POST':
        miformulario = ProfesoresFormulario(request.POST)
        print(miformulario)
        if miformulario.is_valid:
            informacion= miformulario.cleaned_data
            profesores = Profesores(nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email'], materia=informacion['profesion'])
            profesores.save()
            return render(request, 'inicio.html')
    else:
        miformulario = ProfesoresFormulario()
    return render(request, 'profesoresformulario.html', {'miformulario': miformulario})

#Alumnos
def alumnos(request):
    return render(request, "alumnos.html")

def alumnosformulario (request):
    if request.method == 'POST':
        miformulario = AlumnosFormulario(request.POST)
        print(miformulario)
        if miformulario.is_valid:
            informacion= miformulario.cleaned_data
            alumnos = Alumnos(nombre=informacion['nombre'], apellido=informacion['apellido'], padron=informacion['padron'], email=informacion['email'])
            alumnos.save()
            return render(request, 'inicio.html')
    else:
        miformulario = AlumnosFormulario()
    return render(request, 'alumnosformulario.html', {'miformulario': miformulario})

#Egresados
def egresados(request):
    return render(request, "egresados.html")

def egresadosformulario (request):
    if request.method == 'POST':
        miformulario = EgresadosFormulario(request.POST)
        print(miformulario)
        if miformulario.is_valid:
            informacion= miformulario.cleaned_data
            egresados = Egresados(nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email'], profesion=informacion['profesion'])
            egresados.save()
            return render(request, 'inicio.html')
    else:
        miformulario = EgresadosFormulario()
    return render(request, 'egresadosformulario.html', {'miformulario': miformulario})

#Institucional
def institucional(request):
    return render(request, "institucional.html")

def institucionalformulario (request):
    if request.method == 'POST':
        miformulario = InstitucionalFormulario(request.POST)
        print(miformulario)
        if miformulario.is_valid:
            informacion= miformulario.cleaned_data
            institucional = Institucional(nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email'], cargo=informacion['cargo'])
            institucional.save()
            return render(request, 'inicio.html')
    else:
        miformulario = InstitucionalFormulario()
    return render(request, 'institucionalformulario.html', {'miformulario': miformulario})

#busqueda
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