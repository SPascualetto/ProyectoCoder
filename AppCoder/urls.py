from django.urls import path
from AppCoder import views

urlpatterns = [
    path("", views.inicio),
    path('alumnos', views.alumnos, name="alumnos"),
    path('profesores', views.profesores, name="profesores"),
    path("entregables", views.entregables, name="entregables")
]
                            
