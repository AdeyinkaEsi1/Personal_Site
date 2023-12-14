from django.urls import path
from . import views

# URLCONF
urlpatterns = [
    path('home', views.home, name='home'),
    path('resume', views.resume, name='resume'),
    path('projects', views.projects, name='projects'),
    path('contact', views.contact, name='contact'),
    ]
