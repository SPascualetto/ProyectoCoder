from django.urls import path, include
from AppCoder import views
from django.contrib.auth.views import LogoutView

app_name = 'AppCoder'


urlpatterns = [
    path('', views.inicio, name='Inicio'),
    path('cursos', views.cursos, name='Cursos'),
    path('profesores', views.profesores, name='Profesores'),
    path('estudiantes', views.estudiantes, name='Estudiantes'),
    path('entregables', views.entregables, name='Entregables'),
    #path('cursoFormulario', views.cursoFormulario, name='CursoFormulario'),
    path('profesorFormulario', views.profesorFormulario, name='ProfesorFormulario'),
    path('busquedaCamada', views.busquedaCamada, name='BusquedaCamada'),
    path('buscar/', views.buscar),
    path('leerCursos', views.leerCursos, name="LeerCursos"),
    path('curso/list', views.CursoList.as_view(), name='List'),
    path('<int:pk>', views.CursoDetalle.as_view(), name='Detail'),
    path('nuevo', views.CursoCreacion.as_view(), name='New'),
    path('editar/<int:pk>', views.CursoUpdate.as_view(), name='Edit'),
    path('borrar/<int:pk>', views.CursoDelete.as_view(), name='Delete'),
    path('leerProfesores', views.leerProfesores, name='LeerProfesores'),
    path('eliminarProfesor/<profesor_nombre>/',views.eliminarProfesor, name="EliminarProfesor"),
    path('editarProfesor/<profesor_nombre>', views.editarProfesor, name='EditarProfesor'),
    path('login', views.login_request, name='Login'),
    path('register', views.register, name='Registro'),
    path('logout', LogoutView.as_view(template_name='logout.html'), name='Logout'),
    path('editarPerfil', views.editarPerfil, name='EditarPerfil'),
    path('agregarAvatar', views.agregarAvatar, name='AgregarAvatar'),
]
