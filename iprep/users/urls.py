from django.urls import path
from .models import *
from .views import *
urlpatterns = [
    path('home/', HomeView.as_view(), name='user_home'),
    path('',UserRegistration.as_view()),
    path('login/',CustomLoginView.as_view(),name = 'home')
]