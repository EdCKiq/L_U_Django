from django.shortcuts import render, get_object_or_404
from .models import Itens
from django.http import HttpResponse
from django.template import loader
from datetime import date
from django.utils import timezone

def index(request):
    data = date.today()
    data_time = timezone.now()
    itens = Itens.objects.all()
    context = {
        'itens': itens,
        'data': data,
        'data_time': data_time
    }
    return render(request,'index.html',context)

def about_us(request):
    return render(request, 'about_us.html')

def item(request, code_item):
    #itens = Itens.objects.get(code_item = code_item) # Sem tratamento de erro
    itens = get_object_or_404(Itens, code_item = code_item) # Com tratamento de erro
    context = {
        'itens': itens
    }
    return render(request, 'item.html', context)

def error404(request, ex):
    template = loader.get_template('Error404.html')
    return HttpResponse(content = template.render(),content_type = 'text/html; charset=UTF8', status = 404 )

def error500(request):
    template = loader.get_template('Error500.html')
    return HttpResponse(content= template.render(), content_type = 'text/html; charset = UTF8', status = 500)