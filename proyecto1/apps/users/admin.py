from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.
class CustomUserAdmin(UserAdmin):
    model=User
    
    list_display = ('email', 'usertype', 'image', 'nombre', 'apellidos', 'create_at')
    
    list_filter = ('email', 'usertype', 'image', 'nombre', 'apellidos', 'create_at')
    
    fieldsets = ((None, {'fields': ('email', 'usertype', 'image', 'nombre', 'apellidos', 'password')}), ('Permissions', {'fields': ('is_active', 'is_staff')}))

    add_fieldsets = ( (None, { 'classes': ('wide',), 'fields': ('email', 'usertype', 'image', 'nombre', 'apellidos', 'password1', 'password2', 'is_active', 'is_staff')}), ) 
    
    ordering = ('email',)
    
    
admin.site.register (User, CustomUserAdmin)
