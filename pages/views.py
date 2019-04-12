from django.shortcuts import render
from pages.forms import HomeForms
from usuario.models import Usuario
from publicacion.models import Publicacion
from comments.models import Comments
from django.shortcuts import render
from django.views.generic import TemplateView


def index(request):
    usuario = Usuario.objects.all()
    publicacion = Publicacion.objects.all()
    context = {
        'usuario': usuario,
        'publicacion': publicacion
    }
    return render(request, 'pages/index.html', context)



def about(request):
    return render(request, 'pages/publicacion.html')

def perfil(request):
    usuario = Usuario.objects.all()
    publicacion = Publicacion.objects.all()
    comments = Comments.objects.all()
    context = {
        'usuario': usuario,
        'publicacion': publicacion,
        'comentarios':comments
    }
    return render(request, 'pages/perfil.html', context)

def subirpub(request):
    return render(request, 'pages/subirpublicacion.html')

def seguidores(request):
    return render(request, 'pages/seguidores.html')

class HomeView(TemplateView):
    template_name = 'home/home.html'

    def get(self, request):
        form = HomeForms()
        return render(request, self.template_name, {'form': form})