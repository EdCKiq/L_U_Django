from django import forms
from django.core.mail.message import EmailMessage

class ContatoForm(forms.Form):
    nome = forms.CharField(label='Seu Nome', max_length=100)
    email = forms.EmailField(label='Seu Email', max_length=100)
    assunto = forms.CharField(label='Assunto', max_length=100)
    mensagem = forms.CharField(label='Mensagem',max_length=300,widget=forms.Textarea())

    def enviar_email(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']

        email_base = f'Olá {nome}, recebemos o seu e-mail intitulado {assunto}\nAssim estamos retornando para esse email: {email} uma confirmação e uma cópia da messagem\nMensagem: {mensagem}'

        mail = EmailMessage(
            subject = assunto,
            body = email_base,
            from_email = 'contatofusion@fusion.com.br',
            to = ['contatofusion@fusion.com.br',],
            headers = {'Reply-To':email}
        )
        
        mail.send()
