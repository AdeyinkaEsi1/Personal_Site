
from django.shortcuts import render
# from .models import MyResume

def home(request):
    # resume = MyResume.objects.all()
    return render(request, 'mysite/home.html')

def resume(request):
    # cv = MyResume.objects.all()
    return render(request, 'mysite/resume.html')

def projects(request):
    return render(request, 'mysite/projects.html')

def contact(request):
    return render(request, 'mysite/contact.html')
