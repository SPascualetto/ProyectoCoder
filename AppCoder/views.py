from django.shortcuts import render

def inicio(request):
    return render(request, "inicio.html")

def profesores(request):
    return render(request, "profesores.html")

def alumnos(request):
    return render(request, "alumnos.html")

def entregables(request):
    return render(request, "entregables.html")