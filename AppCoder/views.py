from django.shortcuts import render

def inicio(request):
    return render(request, "appcoder/inicio.html")

def cursos(request):
   return render(request, "appcoder/cursos.html")

def profesores(request):
    return render(request, "appcoder/profesores.html")

def estudiantes(request):
    return render(request, "appcoder/estudiantes.html")

def entregables(request):
    return render(request, "appcoder/entregables.html")