from django.contrib.auth import authenticate
from .models import User
from django import forms


class LoginForm (forms.Form):
    
    email = forms.CharField(
        label = 'Email', 
        required = True,
        widget = forms.TextInput(
            attrs = {
                'placeholder' : 'Email'
            }
        )
    )
    
    password = forms.CharField(
        label = 'Contraseña', 
        required = True,
        widget = forms.PasswordInput(
            attrs = {
                'placeholder' : '***********'
            }
        )
    )
    
        
    def clean (self):
        cleaned_data = super(LoginForm, self).clean()
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']
        
        if not authenticate(email=email, password=password):
            raise forms.ValidationError('los datos son incorrectoss, intente de nuevo...')
        
        return self.cleaned_data
        