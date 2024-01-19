from django.shortcuts import render, redirect
from .models import Categoria, Flashcard
from django.contrib.messages import constants
from django.contrib import messages

# Create your views here.
def novo_flashcard(request):
    if not request.user.is_authenticated:
        return redirect('/usuarios/logar')
    
    if request.method == "GET":
        categoria = Categoria.objects.all()
        dificuldades = Flashcard.DIFICULDADE_CHOICES
        flashcards = Flashcard.objects.filter(user = request.user)

        return render(request, 'novo_flashcard.html', {'categorias': categoria, 'dificuldades': dificuldades, 'flashcards': flashcards})
    
    elif request.method == "POST":
        pergunta = request.POST.get('pergunta')
        resposta = request.POST.get('resposta')
        categoria = request.POST.get('categoria')
        dificuldade = request.POST.get('dificuldade')

        if len(pergunta.strip()) == 0 or len(resposta.strip()) == 0:
            messages.add_message(request, constants.ERROR, 'Preencha os campos corretamente!')
            return redirect ('/flashcard/novo_flashcard/')
        
        
        
        flashcard = Flashcard (
            user = request.user,
            pergunta = pergunta,
            resposta = resposta,
            categoria_id  = categoria
        )

        flashcard.save()

        messages.add_message(request, constants.SUCCESS, 'Flashcard cadastrado com sucesso!')
        return redirect('/flashcard/novo_flashcard')
            
