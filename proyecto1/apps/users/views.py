from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import *
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.views.generic import View



class LoginViews(FormView): 
    template_name = "login.html"
    form_class = LoginForm
    success_url = reverse_lazy ('biblioteca_app:list_libros')
    
    def form_valid (self, form):
        user = authenticate(
            email = form.cleaned_data ['email'], 
            password = form.cleaned_data['password']
            )
        
        login(self.request, user)
        
        return super (LoginViews, self).form_valid (form)

    
class LogoutView(View):
    def get(elf, request, *args, **kargs):
        logout(request)
        return HttpResponseRedirect(
            reverse(
                'users_app:login'
            )
        )
        
        
    # Create your views here.
