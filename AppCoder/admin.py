from django.contrib import admin
from .models import Alumnos, Profesores, Egresados, Institucional

admin.site.register(Alumnos)
admin.site.register(Profesores)
admin.site.register(Egresados)
admin.site.register(Institucional)
