from django import forms
from django.core.mail.message import EmailMessage
from .models import Livros
from datetime import datetime

class LivrosForm(forms.Form):
    nome = forms.CharField(label="Nome do livro")
    email = forms.EmailField(label="Seu E-mail")
    coment = forms.CharField(label="Porque deve ser adicionado?", widget=forms.Textarea())

    def send_email(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        coment = self.cleaned_data['coment']

        content = f'O livro {nome}!\nLFoi enviado para analise\nPorque deve ser adicionado?:\n{coment}.\nLogo retornaremos com uma resposta'

        mail = EmailMessage(
            subject ="Livro Adicionado", # Assunto
            body = content, # Conteúdo do email
            from_email = "contato@seudominio.com", # Email que vai enviar o email
            to = ['contato@seudominio.com',], 
            headers = {'Reply to': email} # Para qual email será enviado a resposta
        )
        mail.send()


class LivrosModelForm(forms.ModelForm):
    class Meta:
        model = Livros
        fields = ['nome', 'preco', 'estoque', 'solicitado', 'imagem']