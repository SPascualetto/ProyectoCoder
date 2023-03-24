from django.contrib.auth.forms import UserChangeForm, UserCreationForm, PasswordChangeForm
from django import forms
from django.contrib.auth.models import User 
from AppCoder.models import Alumnos, Comentario

class FormularioRegistroUsuario(UserCreationForm):
    first_name = forms.CharField(max_length=20, label='Nombre', widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=20, label='Apellido', widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    username = forms.CharField(max_length=20, label='Usuario', widget=forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Repita Contraseña', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = User
        fields = ('email', 'username', 'first_name', 'last_name', 'password1', 'password2')


class FormularioEdicion(UserChangeForm):
    password = None
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=20, label='Nombre', widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=20, label='Apellido', widget=forms.TextInput(attrs={'class':'form-control'}))
    username = forms.CharField(max_length=20, label='Usuario', widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('email', 'username', 'first_name', 'last_name')

class AlumnosFormulario(forms.ModelForm):
    class Meta:
        model = Alumnos
        fields = ('usuario', 'nombre', 'apellido', 'padron')

        widgets = {
            'usuario': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id':'usuario_id', 'type':'hidden'}),
            'nombre' : forms.TextInput(attrs={'class': 'form-control'}),
            'apellido' : forms.TextInput(attrs={'class': 'form-control'}),
            'padron' : forms.TextInput(attrs={'class': 'form-control'}),
            }

class AlumnosActualizacion(forms.ModelForm):
    class Meta:
        model = Alumnos
        fields = ('usuario', 'padron')

        widgets = {
            'usuario': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id':'usuario_id', 'type':'hidden'}),
            'facultad' : forms.TextInput(attrs={'class': 'form-control'}),
            'carrera' : forms.Select(attrs={'class': 'form-control'}),
            'sede' : forms.TextInput(attrs={'class': 'form-control'}),
            'padron' : forms.TextInput(attrs={'class': 'form-control'}),
        }

class FormularioComentario(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ('nombre', 'mensaje')
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'mensaje' : forms.Textarea(attrs={'class': 'form-control'}),
        }

class FormularioPassCambio(PasswordChangeForm):
    old_password = forms.CharField(label=("Password Actual"),
                                   widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password1 = forms.CharField(label=("Nuevo Password"),
                                   widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password2 = forms.CharField(label=("Repita Nuevo Password"),
                                   widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')