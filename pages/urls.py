from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('publicacion', views.about, name='publicacion'),
    path('admin', views.about, name='admin'),
    path('perfil', views.perfil, name='perfil'),
    path('subirpublicacion', views.subirpub, name='subirpublicacion'),
    path('seguidores', views.seguidores, name='seguidores'),

]
