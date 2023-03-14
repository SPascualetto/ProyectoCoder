from django.urls import path
from AppCoder import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path('alumnos/', views.alumnos, name="alumnos"),
    path('profesores/', views.profesores, name="profesores"),
    path("egresados/", views.egresados, name="egresados"),
    path("institucional/", views.institucional, name="institucional"),
    path('profesoresformulario', views.profesoresformulario, name='profesoresformulario'),
    path('alumnosformulario', views.alumnosformulario, name='alumnosformulario'),
    path('egresadosformulario', views.egresadosformulario, name='egresadosformulario'),
    path('institucionalformulario/', views.institucionalformulario, name='institucionalformulario'),
    path('buscar/', views.buscar, name="buscar")
]
                            