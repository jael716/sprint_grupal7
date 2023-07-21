from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import TareaForm
from .models import Tarea
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import FiltroTareaForm


# Create your views here.

def welcome(request):
    return render(request, "home.html")



class TareaListView(LoginRequiredMixin, ListView):
    model = Tarea
    template_name = 'tarea_list.html'
    context_object_name = 'tareas'

    def get_queryset(self):
        queryset = super().get_queryset().filter(asignado_a=self.request.user)
        form = FiltroTareaForm(self.request.GET)
        if form.is_valid():
            if form.cleaned_data['estado']:
                queryset = queryset.filter(estado=form.cleaned_data['estado'])
            if form.cleaned_data['etiqueta']:
                queryset = queryset.filter(label=form.cleaned_data['etiqueta'])
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = FiltroTareaForm(self.request.GET)
        return context

class TareaDetailView(LoginRequiredMixin, DetailView):
    model = Tarea
    template_name = 'tarea_detail.html'


@login_required
def tarea_crear(request):
    if request.method == "POST":
        form = TareaForm(request.POST)
        if form.is_valid():
            tarea = form.save(commit=False)
            tarea.asignado_a = request.user
            tarea.save()
            return redirect('tarea_detail', pk=tarea.pk)
    else:
        form = TareaForm()
    return render(request, 'tarea_form.html', {'form': form})



class TareaUpdateView(LoginRequiredMixin, UpdateView):
    model = Tarea
    form_class = TareaForm
    template_name = 'tarea_form.html'
    
    def get_success_url(self):
        return reverse_lazy('lista_tarea')


class TareaDeleteView(LoginRequiredMixin, DeleteView):
    model = Tarea
    template_name = 'delete.html'
    
    def get_success_url(self):
        return reverse_lazy('lista_tarea')
    

def completar_tarea(request, pk):
    tarea = Tarea.objects.get(pk=pk, asignado_a=request.user)
    tarea.estado = 'C'  
    tarea.save()
    return redirect('tarea_detail', pk=pk)