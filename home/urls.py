from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dicas_treino', views.dicas_treino, name='dicas_treino'),
    path('cadastro_treino', views.cadastro_treino, name='cadastro_treino'),
   path('editar_treino/<int:id_treino', views.editar, name='editar_treino'),
]