from django.urls import path 
from .views import *

app_name = 'users_app'
urlpatterns = [ 
	path ('login', LoginViews.as_view(), name = 'login'),
	path ('logout', LogoutView.as_view(), name = 'logout'),
 
] 