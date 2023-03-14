from django import forms

class AlumnosFormulario(forms.Form):

    nombre= forms.CharField()
    apellido= forms.CharField()
    padron= forms.IntegerField( )
    email =forms.EmailField()

class ProfesoresFormulario(forms.Form):
    nombre =forms.CharField(max_length=30)            
    apellido =forms.CharField(max_length=30)
    email =forms.EmailField()
    materia= forms.CharField(max_length=30) 


class EgresadosFormulario(forms.Form):
    nombre =forms.CharField(max_length=30)         
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
    profesion= forms.CharField(max_length=30) 


class InstitucionalFormulario(forms.Form):
    nombre= forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
    cargo= forms.CharField(max_length=30) 