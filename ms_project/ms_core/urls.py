from django.urls import path
from .views import index, pedidos_livros, compradores, loja_livros

urlpatterns = [
    path('', index, name= 'index'),
    path('pedidos/', pedidos_livros, name='pedidos'),
    path('compradores/', compradores, name='compradores'),
    path('loja/', loja_livros, name='loja')
]