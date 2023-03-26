from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date

class Post(models.Model):
    Titulo=models.CharField(max_length=255)
    Carrera = models.CharField(max_length=255)
    Nombre=models.ForeignKey(User, on_delete=models.CASCADE)
    Cuerpo = models.TextField()
    post_date=models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.title  + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        return reverse('home')
