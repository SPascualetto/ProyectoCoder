from django.urls import path
from AppCoder import views

urlpatterns = [
    path("", views.inicio),
    path('alumnos', views.alumnos),
    path('profesores', views.profesores),
    path("entregables", views.entregables)
]
                            