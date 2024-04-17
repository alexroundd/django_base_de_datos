from .models import *
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy



class StaffRequiredMixin (UserPassesTestMixin):
    def test_func (self):
        if self.request.user:
            return self.request.user.usertype == 'editor' or self.request.user.usertype == 'administrator'
        
    def handle_no_permission (self):
        return redirect(reverse_lazy ('users_app:login'))
             