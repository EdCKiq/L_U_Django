from django.db import models

class User(models.Model):
    nome_user = models.CharField("Nome",max_length=50)
    sobrenome_user = models.CharField("Sobrenome", max_length=100)
    email_user = models.EmailField("Email",max_length=100)
    idade_user = models.IntegerField("Idade")

    def __str__(self):
        return self.nome_user # Retorna o nome do user na tela principal do admin

class Itens(models.Model):
    nome_item = models.CharField("Nome",max_length=100)
    code_item = models.CharField("Código", max_length=200,primary_key=True)
    preco_item = models.DecimalField("Preço",max_digits=7,decimal_places=2)

    def __str__(self):
        return self.nome_item #Retorna o nome do item na tela principal do admin