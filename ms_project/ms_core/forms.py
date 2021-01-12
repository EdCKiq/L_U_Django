from django import forms
from django.core.mail.message import EmailMessage

class LivrosForm(forms.Form):
    nome = forms.CharField(label="Nome do livro")
    email = forms.EmailField(label="Seu E-mail")
    ano_publi = forms.IntegerField(label="Ano de Publicação")
    coment = forms.CharField(label="O que achou do livro?", widget=forms.Textarea())

    def send_email(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        ano_publi = self.cleaned_data['ano_publi']
        coment = self.cleaned_data['coment']

        content = f'O livro {nome}!\nLançado em {ano_publi} foi adicionado\nSeu comentário sobre ele:\n{coment}.'

        mail = EmailMessage(
            subject ="Livro Adicionado", # Assunto
            body = content, # Conteúdo do email
            from_email = "contato@seudominio.com", # Email que vai enviar o email
            to = ['contato@seudominio.com',], 
            headers = {'Reply to': email} # Para qual email será enviado a resposta
        )
        mail.send()
