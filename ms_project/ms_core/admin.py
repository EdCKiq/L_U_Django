from django.contrib import admin
from .models import Livros

#Registrando no Admin com decorator
@admin.register(Livros)
class LivrosAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque', 'slug')