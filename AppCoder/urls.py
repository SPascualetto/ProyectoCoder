from django import views
from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views
from .views import Login, Registro, UsuarioEditar, PassCambio, PassOK

urlpatterns = [
    #Inicio
    path('login/', Login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(template_name='base/logout.html'), name='logout'),
    path('registro/', Registro.as_view(), name='registro'),
    path('edicionPerfil/', UsuarioEditar.as_view(), name='editar_perfil'),
    path('passCambio/', PassCambio.as_view(), name='cambiar_password'),
    path('passOk/' , views.PassOK, name='password_exitoso'),
      
    #Profesores
    path('profesores/', views.Profesores, name="Profesores"),
    path('profesoresLista', views.ProfesoresLista.as_view(), name="ProfesoresLista"), 
    path('profesoresDetalle', views.ProfesoresDetalle.as_view(), name="ProfesoresDetalle"),    
    path('profesoresUpdate/<int:pk>/', views.ProfesoresUpdate.as_view(), name="ProfesoresUpdate"), 
    path('profesoresDelete/<int:pk>/', views.ProfesoresDelete.as_view(), name="ProfesoresDelete"),
   
    #Alumnos
    path('alumnos/', views.Alumnos, name="Alumnos"),
    path('alumnosLista', views.AlumnosLista.as_view(), name="AlumnosLista"), 
    path('alumnosDetalle', views.AlumnosDetalle.as_view(), name="AlumnosDetalle"),    
    path('alumnosUpdate/<int:pk>/', views.AlumnosUpdate.as_view(), name="AlumnosUpdate"), 
    path('alumnosDelete/<int:pk>/', views.AlumnosDelete.as_view(), name="AlumnosDelete"),
       
    #Egresados
    path('egresados/', views.Egresados, name="Egresados"),
    path('egresadosLista', views.EgresadosLista.as_view(), name="EgresadosLista"), 
    path('egresadosDetalle', views.EgresadosDetalle.as_view(), name="EgresadosDetalle"),    
    path('egresadosUpdate/<int:pk>/', views.EgresadosUpdate.as_view(), name="EgresadosUpdate"), 
    path('egresadosDelete/<int:pk>/', views.EgresadosDelete.as_view(), name="EgresadosDelete"),
   
    
    #Institucional
    path('institucional/', views.Institucional, name="Institucional"),
    path('institucionalLista', views.InstitucionalLista.as_view(), name="InstitucionalLista"), 
    path('institucionalDetalle', views.InstitucionalDetalle.as_view(), name="InstitucionalDetalle"),    
    path('institucionalUpdate/<int:pk>/', views.InstitucionalUpdate.as_view(), name="InstitucionalUpdate"), 
    path('institucionalDelete/<int:pk>/', views.InstitucionalDelete.as_view(), name="InstitucionalDelete"),

    #Buscar
    path('buscar/', views.buscar, name="buscar")
    
]
                            