from django.contrib import admin
from .models import Servico,Cargo,Funcionario,Funcionaliades

@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('nome','icones','ativo','modificacao')

@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ativo','modificacao')

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome','cargo','ativo','modificacao')

@admin.register
class FuncionalidadesAdmin(admin.ModelAdmin):
    list_display = ('nome','icones','ativo','modificado')