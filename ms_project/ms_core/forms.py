from django import forms

class LivrosForm(forms.Form):
    nome = forms.CharField(label="Nome")
    edit_email = forms.EmailField(label="E-mail da editora")
    ano_publi = forms.IntegerField(label="Ano de Publicação")
    coment = forms.CharField(label="Comentários", widget=forms.Textarea())
