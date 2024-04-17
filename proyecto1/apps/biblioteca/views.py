from django.shortcuts import render
from django.views.generic.edit import UpdateView 
from django.views.generic.edit import CreateView 
from .models import Libro
from .forms import LibroForm  
from django.core.mail import send_mail
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from apps.users.helpers import *
from django.db.models import Q

class LibroUpdateView(StaffRequiredMixin, UpdateView): 
    login_url = reverse_lazy ('users_app:login')
    model = Libro 
    template_name = "update.html"
    fields = [ 
		"titulo",
        "autor",
        "año_edicion",
        "tematica",
        "isbn",
        "editorial",
        "descripcion",
	] 
    success_url ="/"
    
    
class LibroCreateView(StaffRequiredMixin, CreateView): 
    login_url = reverse_lazy ('users_app:login')
    model = Libro 
    template_name = "create_view.html"
    fields = [ 
		"titulo",
        "autor",
        "año_edicion",
        "tematica",
        "isbn",
        "editorial",
        "descripcion",
    ] 
    success_url ="/"
    
   
@login_required (login_url = 'users_app:login')    
def list_view(request):
    context ={}
 
    # add the dictionary during initialization
    context["dataset"] = Libro.objects.all()

    return render(request, "lista_libro.html", context)


def list_view(request):
    context = {}

    if 'query' in request.GET:
        query = request.GET.get('query')
        libros = Libro.objects.filter(
            Q(tituloicontains=query) |
            Q(autornameicontains=query) |
            Q(tematicanombreicontains=query) |
            Q(isbnicontains=query)
        )
        context['query'] = query
        context['dataset'] = libros
    else:
        context['dataset'] = Libro.objects.all()

    return render(request, "lista_libro.html", context)
class BuscarLibroForm(forms.Form):
    query = forms.CharField(label='Buscar', max_length=100)


# Create your views here.
