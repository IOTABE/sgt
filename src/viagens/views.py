from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from django. http import HttpResponseRedirect
from django.contrib import messages
from .models import Viagens
from .forms import ViagensForm


def cad_viagem(request):

    form = ViagensForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Agendamento cadastrado com sucesso!!")
        return HttpResponseRedirect('/')
    
    return render(request, "viagens_form.html", {'form': form})


class ViagensListView(ListView):
    model = Viagens
    context_object_name = 'viagens'
 
 
class ViagensCreateView(CreateView):
    model = Viagens
    fields = '__all__'
       
    
class ViagensUpdateView(UpdateView):
    model = Viagens
    fields = '__all__'
    success_url = reverse_lazy('t_lista')
    
    
class ViagensDeleteView(DeleteView):
    queryset = Viagens.objects.all()
    success_url = reverse_lazy('t_lista')


class ViagensDetailView(DetailView):
    queryset = Viagens.objects.all()