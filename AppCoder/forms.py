from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model =Post
        fields = ('Titulo', 'Carrera', 'Nombre', 'Cuerpo' )
        
        widgets ={
            
            'Titulo': forms.TextInput(attrs={'class': 'forms-control'}),
            'Carrera': forms.TextInput(attrs={'class': 'forms-control'}),
            'Nombre': forms.Select(attrs={'class': 'forms-control'}),
            'Cuerpo': forms.Textarea(attrs={'class': 'forms-control'}),
        }       

class EditForm(forms.ModelForm):
    class Meta:
        model =Post
        fields = ('Titulo','Carrera', 'Cuerpo' )
        
        widgets ={
            'Titulo': forms.TextInput(attrs={'class': 'forms-control'}),
            'Referencia': forms.TextInput(attrs={'class': 'forms-control'}),
            'Cuerpo': forms.Textarea(attrs={'class': 'forms-control'}),     
        }