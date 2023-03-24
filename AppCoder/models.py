from django.db import models
from django.contrib.auth.models import User

class Alumnos(models.Model):
    alumnoSeleccion = (
    ('nombre','Nombre'),
    ('apellido', 'Apellido'),
    ('padron','Padron'),
    ('email','Email'),
    
    )
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=40)
    padron = models.IntegerField() 
    email = models.EmailField()
    fotodni = models.ImageField(null=True, blank=True, upload_to="imagenes/")

    class Meta:
        ordering = ['usuario', 'padron']

    def __str__(self):
        return self.padron

class Profesores(models.Model):
    profesoresSeleccion = (
    ('nombre','Nombre'),
    ('apellido', 'Apellido'),
    ('materia','Materia'),
    ('email','Email'),
    
    )
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=40)
    materia = models.CharField(max_length=40)
    email = models.EmailField()
    fotodni = models.ImageField(null=True, blank=True, upload_to="imagenes/")

    class Meta:
        ordering = ['usuario', 'materia']

    def __str__(self):
        return self.materia
    
class Egresados(models.Model):
    egresadosSeleccion = (
    ('nombre','Nombre'),
    ('apellido', 'Apellido'),
    ('profesion','Profesion'),
    ('email','Email'),
    
    )
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=40)
    profesion = models.CharField(max_length=40)
    email = models.EmailField()
    fotodni = models.ImageField(null=True, blank=True, upload_to="imagenes/")

    class Meta:
        ordering = ['usuario', 'profesion']

    def __str__(self):
        return self.profesion

class Institucional(models.Model):
    institucionalSeleccion = (
    ('nombre','Nombre'),
    ('apellido', 'Apellido'),
    ('cargo','Cargo'),
    ('email','Email'),
    
    )
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=40)
    cargo = models.CharField(max_length=40)
    email = models.EmailField()
    fotodni = models.ImageField(null=True, blank=True, upload_to="imagenes/")

    class Meta:
        ordering = ['usuario', 'cargo']

    def __str__(self):
        return self.cargo
    
class Comentario(models.Model):
    comentario = models.ForeignKey(Alumnos, related_name='comentarios', on_delete=models.CASCADE, null=True)
    nombre = models.CharField(max_length=40)
    mensaje = models.TextField(null=True, blank=True)
    fechaComentario = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fechaComentario']

    def __str__(self):
        return '%s - %s' % (self.nombre, self.comentario)