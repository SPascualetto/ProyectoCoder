from django.db import models
    
class Alumnos(models.Model):
    nombre= models.CharField(max_length=40)
    apellido= models.CharField(max_length=40)
    padron= models.IntegerField()
    email= models.EmailField(max_length=30)
    
    def _str_(self):
        return f"nombre:{self.nombre} - apellido:{self.apellido} - padron:{self.padron} - email: {self.email}"


class Profesores(models.Model):
    nombre= models.CharField(max_length=40)
    apellido= models.CharField(max_length=40)
    email= models.EmailField(max_length=30)
    materia= models.CharField(max_length=30)

class Egresados(models.Model):
    nombre= models.CharField(max_length=40)
    apellido= models.CharField(max_length=40)
    email= models.EmailField(max_length=30)
    profesion= models.CharField(max_length=30)
    
class Institucional(models.Model):
    nombre= models.CharField(max_length=40)
    apellido= models.CharField(max_length=40)
    email= models.BooleanField(max_length=30)
    cargo= models.CharField(max_length=40)
    
