from django.urls import path 
from .views import LibroUpdateView 
from .views import LibroCreateView 
from .views import list_view

app_name = 'biblioteca_app'
urlpatterns = [ 
	path('libro/<int:pk>/', LibroUpdateView.as_view(), name = 'libro_update'),
	path('create', LibroCreateView.as_view(), name = 'create_view'),
	path('',list_view, name = "list_libros")
] 
