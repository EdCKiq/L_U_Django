from django.urls import path
from .views import index, about_us, item

# Aqui é feito de forma separada para onde cada comando vai, tornando a url do Projeto mais limpa e de simples leitura

urlpatterns=[
    path('', index, name='index'),
    path('aboutus/', about_us, name='about'),
    path('item/code/<int:code_item>', item, name='item')
]