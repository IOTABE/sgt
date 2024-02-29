from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from django. http import HttpResponseRedirect
from django.contrib import messages
from .models import Motorista, Veiculo, Setores
from .forms import MotoristaForm, VeiculoForm, SetorForm
from django.contrib.auth.decorators import login_required

def home(request):
    
    return render(request, "index.html")

def cad_motorista(request):

    form = MotoristaForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Motorista cadastrado com sucesso!!")
        return HttpResponseRedirect('/')
    
    return render(request, "motorista_form.html", {'form': form})


class MotoristaListView(ListView):
    model = Motorista
    context_object_name = 'motoristas'
 
 
class MotoristaCreateView(CreateView):
    model = Motorista
    fields = ["nome"]
    
    
class MotoristaUpdateView(UpdateView):
    model = Motorista
    fields = '__all__'
    success_url = reverse_lazy('m_lista')
    
    
class MotoristaDeleteView(DeleteView):
    queryset = Motorista.objects.all()
    success_url = reverse_lazy('m_lista')


class MotoristaDetailView(DetailView):
    queryset = Motorista.objects.all()
    
@login_required
def cad_veiculo(request):

    form = VeiculoForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Veiculo cadastrado com sucesso!!")
        return HttpResponseRedirect('/')
    
    return render(request, "veiculo_form.html", {'form': form})


class VeiculoListView(ListView):
    model = Veiculo
    context_object_name = 'veiculos'
 

class VeiculoCreateView(CreateView):
    model = Veiculo
    fields = ["modelo", "placa"]
    
      
class VeiculoUpdateView(UpdateView):
    model = Veiculo
    fields = '__all__'
    success_url = reverse_lazy('v_lista')
    
  
class VeiculoDeleteView(DeleteView):
    queryset = Veiculo.objects.all()
    success_url = reverse_lazy('v_lista')


class VeiculoDetailView(DetailView):
    queryset = Veiculo.objects.all()


def cad_setor(request):

    form = SetorForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Setor cadastrado com sucesso!!")
        return HttpResponseRedirect('/')
    
    return render(request, "setores_form.html", {'form': form})


class SetorListView(ListView):
    model = Setores
    context_object_name = 'setores'
 
 
class SetorCreateView(CreateView):
    model = Setores
    fields = ["setor", "telefone"]
    
    
class SetorUpdateView(UpdateView):
    model = Setores
    fields = '__all__'
    success_url = reverse_lazy('s_lista')
    
    
class SetorDeleteView(DeleteView):
    queryset = Setores.objects.all()
    success_url = reverse_lazy('s_lista')


class SetorDetailView(DetailView):
    queryset = Setores.objects.all()