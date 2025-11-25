from django.shortcuts import render
from .models import Project, Profile

def home(request):
    profile = Profile.objects.first()  # Load the first profile entry
    context = {'profile': profile}
    return render(request, 'portfolioapp/home.html', context)

def projects(request):
    all_projects = Project.objects.all()
    return render(request, 'portfolioapp/projects.html', {'projects': all_projects})

def about(request):
    return render(request, 'portfolioapp/about.html')

def contact(request):
    return render(request, 'portfolioapp/contact.html')
