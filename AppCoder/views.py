from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Post, Avatar
from .forms import PostForm, EditForm
from django.contrib.auth.models import User 
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

class HomeView(ListView):
    model= Post
    template_name='home.html'
    ordering= ['-post_date']

@login_required   
def home(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    print(avatares[0].imagen.url)
    return render(request, 'home.html', {"url":avatares[0].imagen.url})

class ArticleDetailView(DetailView):
    model= Post
    template_name='detalles.html'

class AddPostView(CreateView):
    model= Post
    form_class= PostForm
    template_name='nuevoposteo.html'
    
class UpdatePostView(UpdateView):
    model=Post
    form_class= EditForm
    template_name= 'modificarposteo.html'

class DeletePostView(DeleteView):
    model=Post
    template_name= 'borrarposteo.html'
    success_url= reverse_lazy('home')

class AcercademiView(TemplateView):
    template_name= 'acercademi.html'

