from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Post
from .forms import PostForm, EditForm
from django.urls import reverse_lazy

class HomeView(ListView):
    model= Post
    template_name='home.html'
    ordering= ['-post_date']
    
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