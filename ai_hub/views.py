from django.shortcuts import render
from django.conf import settings
from .models import *

# Create your views here.
def index(request):
    return render(request, 'index.html')

def projects(request):
    return render(request, 'Projects.html')

def blogs(request):
    blogs = Blog.objects.all()
    context = {'blogs': blogs}
    return render(request, 'blog.html', context)

def blog_viewer(request, pk):
    return render(request, 'blog_viewer.html', {'pk': pk})

def apps(request):
    apps = Apps.objects.all()
    context = {'apps': apps}
    return render(request, 'Apps.html', context)

def career(request):
    return render(request, 'Career.html')

def games(request):
    games = Game.objects.all()
    context = {'games': games}
    return render(request, 'Game.html', context)

def events(request):
    meetups = Event.objects.all()
    upcoming = [event for event in meetups if event.is_upcoming()]
    if len(upcoming) == 0:
        upcoming = None 
    past = [event for event in meetups if not event.is_upcoming()]
    context = {'upcoming': upcoming, 'past': past[-2:]}
    return render(request, 'Events.html', context)

def meetups(request):
    meetups = Event.objects.all()
    context = {'meetups': meetups}
    return render(request, 'Meetups.html', context)

def about(request):
    team_members = Team.objects.all()
    context = {'team_members': team_members}
    return render(request, 'about.html', context)