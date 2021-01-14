from django.shortcuts import render
from .forms import LivrosForm
from django.contrib import messages

def index(request):
    return render(request, 'index.html')

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

def compradores(request):
    return render(request, 'compradores.html')

def loja_livros(request):
    return render(request, 'loja_livros.html')