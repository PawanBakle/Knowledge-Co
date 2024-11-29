from django.shortcuts import render
from django.http import response,request
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from .forms import *
from django.urls import reverse_lazy
from django.contrib.auth import login
# Create your views here.

class HomeView(TemplateView):
    template_name = 'users/home.html'
class UserRegistration(CreateView):
    form_class = CustomerForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('user_home')
    def form_valid(self, form):
        # Save the user with the selected role and experience level
        user = form.save(commit=False)
        user.role = form.cleaned_data['role']
        user.experience_level = form.cleaned_data['experience_level']
        user.save()
        login(self.request, user)
        
        return super().form_valid(form)
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect

class CustomLoginView(LoginView):
    def get_success_url(self):
        user = self.request.user

        
        # Default fallback
        return reverse_lazy('home')

