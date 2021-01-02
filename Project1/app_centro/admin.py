from django.contrib import admin

from .models import User, Itens

class UserAdmin(admin.ModelAdmin):
    list_display = ('nome_user','email_user') # Mostra na tela principal quais itens você deseja ver

class ItensAdmin(admin.ModelAdmin):
    list_display = ('nome_item','code_item')

admin.site.register(User, UserAdmin)
admin.site.register(Itens, ItensAdmin)