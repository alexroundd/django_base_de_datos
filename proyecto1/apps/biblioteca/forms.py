from django import forms 
from .models import Libro

class LibroForm(forms.ModelForm): 

    class Meta: 
        model = Libro 
        
        fields = [ 
		    "titulo",
            "autor",
            "año_edicion",
            "tematica",
            "isbn",
            "editorial",
            "descripcion",
        ] 

class BuscarLibroForm(forms.Form):
    query = forms.CharField(label='Buscar', max_length=100)