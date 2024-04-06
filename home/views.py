from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
# Create your views here.
from .models import Treino


def index(request):
    return render(request, 'index.html')

def dicas_treino(request):
    return render(request, 'dicas_treino.html')


def cadastro_treino(request):
    return render(request, 'cadastro_treino.html')

def criarTreino(request):
    nome = request.POST['nome']
    descricao = request.POST['descricao']
    peso = request.POST['preco']
    repeticao = request.POST['repeticao']

    treino = Treino.objects.create(nome=nome, descricao=descricao, peso=peso, repeticao=repeticao)
    treino.save()
    return redirect ('index')

def editar(request, id_treino):
    treino = get_object_or_404(Treino, pk=id_treino)
    return render(request, 'editar_treino.html', {'dados_treino': treino})
 
    
