from django.shortcuts import render
from django.views.generic import FormView
from django.urls import reverse_lazy
from .models import Servico, Funcionario, Funcionaliades
from .forms import ContatoForm
from django.contrib import messages

class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContatoForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        context['servicos'] = Servico.objects.order_by('?').all() # Ordena de forma aleátoria os itens
        context['funcionarios'] = Funcionario.objects.order_by('?').all()
        context['funcionalidades'] = Funcionaliades.objects.order_by('?').all()
        return context

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Formulário com problemas')
        return super(IndexView, self).form_invalid(form, *args, **kwargs)

    def form_valid(self, form, *args, **kwargs):
        form.enviar_email()
        messages.success(self.request, 'Enviado com sucesso')
        return super(IndexView, self).form_valid(form, *args, **kwargs)



