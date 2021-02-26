import uuid
from django.db import models
import stdimage

#Altera o nome da imagem para que não haja conflitos ao subi-las ao banco.
def name_img(instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename
 

class Base(models.Model):
    criacao = models.DateField('Criação',auto_now_add=True)
    modificacao = models.DateField('Modificação',auto_now=True)
    ativo = models.BooleanField('Ativo',default=True)

    class Meta:
        abstract = True

class Servico(Base):
    ICON_CHOICES=(
        ('lni-cog','Engrenagem'),
        ('lni-stats-up','Status'),
        ('lni-users','Usuarios'),
        ('lni-layers','Camadas'),
        ('lni-mobile','Telefone'),
        ('lni-rocket','Foguete')
    )
    nome = models.CharField('Serviço', max_length=100)
    descricao = models.CharField('Descrição',max_length=200)
    icones = models.CharField('Icone', max_length=12, choices=ICON_CHOICES)

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

    def __str__(self):
        return self.nome

class Cargo(Base):
    nome = models.CharField('Cargo',max_length=100)

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

    def __str__(self):
        return self.nome

class Funcionario(Base):
    nome = models.CharField('Nome', max_length=100)
    cargo = models.ForeignKey('core_fusion.Cargo',verbose_name='Cargo',on_delete=models.CASCADE)
    bio = models.CharField('Bio',max_length=200)
    imagem = stdimage.StdImageField('Imagem', upload_to=name_img ,variations={'thumbnail':{'width':480,'height':480,'crop':True}})
    facebook = models.CharField('Facebook', max_length=100, default='#')
    instagram = models.CharField('Instagram', max_length=100,default='#')
    twitter = models.CharField('Twitter', max_length=100,default='#')

    class Meta:
        verbose_name='Funcionário'
        verbose_name_plural ='Funcionários'

    def __str__(self):
        return self.nome 

class Funcionaliades(Base):
    nome = models.CharField('Nome',max_length=100)
    ICON_CHOICES=(
        ('lni-rocket','Foguete'),
        ('lni-laptop-phone','Laptop-Mobile'),
        ('lni-cog','Engrenagem'),
        ('lni-leaf','Folha'),
        ('lni-layers','Camadas'),
        ('lni-leaf','Folha')
    )
    icon = models.CharField('Icones', max_length=16,choices=ICON_CHOICES)
    descricao = models.TextField('Descrição',max_length=200)

    class Meta:
        verbose_name='Funcionalidade'
        verbose_name_plural = 'Funcionalidades'

    def __str__(self):
        return self.nome 