from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def livros(request):
    return render(request, 'livros.html')

def compradores(request):
    return render(request, 'compradores.html')