from django.db import models
from django.db.models.fields import CharField, DateField, DecimalField
from django.template.context import make_context
from stdimage.models import StdImageField

#Signals
from django.db.models import signals
from django.template.defaultfilters import slugify

#Class que da informações básicas para outras classes 
class Base(models.Model):
    criacao = models.DateField("Data da criação", auto_now_add=True)
    modificacao = models.DateField("Data da modificação", auto_now=True)
    ativo = models.BooleanField("Ativo? ", default=True)
    class Meta():
       abstract = True # Torna a Class abstrata, ou seja, vai servir de base para outras

class Livros(Base):
    nome = models.CharField("Nome",max_length=20)
    preco = models.DecimalField("Preço",max_digits=8,decimal_places=2)
    ano_publi = models.IntegerField("Ano de publicação")
    estoque = models.IntegerField("Estoque")
    solicitado = models.BooleanField("Solicitado?", default=False)
    imagem = StdImageField("Imagem", upload_to='livros', variations={'thumb': (124,124) })
    slug = models.SlugField("Slug", max_length=100, blank=True, editable=False)

    def __str__(self):
        return self.nome

def livros_pre_save(signal,instance,sender,**kwargs):
    instance.slug = slugify(instance.nome)

signals.pre_save.connect(livros_pre_save,sender=Livros)