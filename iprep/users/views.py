from django.shortcuts import render
from django.http import response,request
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout
from .forms import *
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth import login
# Create your views here.

# class HomeView(TemplateView):
#     template_name = 'users/home.html'
# class UserRegistration(CreateView):
#     form_class = CustomerForm
#     template_name = 'users/register.html'
#     success_url = reverse_lazy('login')
#     def form_valid(self, form):
#         # Save the user with the selected role and experience level
#         user = form.save(commit=False)
#         user.role = form.cleaned_data['role']
#         user.experience_level = form.cleaned_data['experience_level']
#         user.save()
#         login(self.request, user)
        
#         return super().form_valid(form)

def homeView(request):
    return render(request,'users/home.html')
def register(request):
    if request.method == 'POST':
        # for registration, get post data
        form = CustomerForm(request.POST)
        # user = form.save(commit=False)
        if form.is_valid():
            form.clean()
            form.save()
            return redirect('logus')
    form = CustomerForm()
    return render(request,'users/register.html',{'form':form})
def user_login(request):
    if request.method == 'POST':
        form  = LoginPage(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username = username,password = password)
            login(request,user)
            
                
            return redirect('user_home')
    else:
        form = LoginPage()
    return render(request,'users/login.html',{'form':form})
# from django.contrib.auth.views import LoginView


# class CustomLoginView(LoginView):
#     form_class = LoginPage
#     template_name = 'users/login.html'
#     success_url = reverse_lazy('user_home')
#     def login(self,form):
        
#         username = self.request.POST['email']
#         password = self.request.POST['password']
       
#         auth = authenticate(username = username,password = password)
#         login(self.request,auth)
        

        
        # Default fallback
     #   return reverse_lazy('login')

