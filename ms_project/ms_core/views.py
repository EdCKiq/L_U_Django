from django.shortcuts import render
from .forms import LivrosForm
from django.contrib import messages

def index(request):
    return render(request, 'index.html')

def livros(request):
    forms = LivrosForm(request.POST or None)
    if str(request.method) == "POST":
        if forms.is_valid():
            nome = forms.cleaned_data['nome']
            edit_email = forms.cleaned_data['edit_email']
            ano_publi = forms.cleaned_data['ano_publi']
            coment = forms.cleaned_data['coment']
            
            messages.success(request,"Enviado com Sucesso!!")

            forms = LivrosForm()

            #print(request.POST) Pode usar para saber seus dados então sendo enviados de forma correta 
        else:
            messages.error(request,"Erro no envio")
            
    context = {
        "forms": forms
    }
    return render(request, 'livros.html', context)

def compradores(request):
    return render(request, 'compradores.html')