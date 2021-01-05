from django.urls import path
from .views import index, livros, compradores

urlpatterns = [
    path('', index, name= 'index'),
    path('livros/', livros, name='livros'),
    path('compradores/', compradores, name='compradores'),
]