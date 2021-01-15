from django.shortcuts import render
from .forms import LivrosForm, LivrosModelForm
from django.contrib import messages
from .models import Livros

def index(request):
    context = {
        'livros': Livros.objects.all(),
    }
    return render(request, 'index.html', context)

def pedidos_livros(request):
    forms = LivrosForm(request.POST or None)
    if str(request.method) == "POST":
        if forms.is_valid():
            forms.send_email()
            messages.success(request,"Enviado com Sucesso!!")

            forms = LivrosForm()

            #print(request.POST) Pode usar para saber seus dados então sendo enviados de forma correta 
        else:
            messages.error(request,"Erro no envio")
            
    context = {
        "forms": forms
    }
    return render(request, 'pedidos_livros.html', context)


def loja_livros(request):
    if str(request.method) == "POST":
        form = LivrosModelForm(request.POST, request.FILES) #request.FILES porque agora temos imagem
        if form.is_valid():
            form.save() # Salva as informações do form para uso no BD
            messages.success(request, "Enviado com sucesso")
            form = LivrosModelForm()
        else:
            messages.error(request, "Erro no envio")
    else:
        form = LivrosModelForm()
    
    context={
        "form":form
    }

    return render(request, 'loja_livros.html', context)