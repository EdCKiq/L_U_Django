from django.urls import path
from .views import index, pedidos_livros, loja_livros

urlpatterns = [
    path('', index, name= 'index'),
    path('pedidos/', pedidos_livros, name='pedidos'),
    path('loja/', loja_livros, name='loja'),
]