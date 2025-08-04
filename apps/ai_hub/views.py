from django.shortcuts import render
from django.conf import settings
from .models import *
import json

# Create your views here.
def index(request):
    return render(request, 'ai_hub/index.html')

def projects(request):
    return render(request, 'ai_hub/Projects.html')

def blogs(request):
    blogs = Blog.objects.all()
    context = {'blogs': blogs}
    return render(request, 'ai_hub/blog.html', context)

def blog_viewer(request, pk):
    return render(request, 'ai_hub/blog_viewer.html', {'pk': pk})

def apps(request):
    apps = Apps.objects.all()
    context = {'apps': apps}
    return render(request, 'ai_hub/Apps.html', context)

def career(request):
    return render(request, 'ai_hub/Career.html')

def games(request):
    games = Game.objects.all()
    context = {'games': games}
    return render(request, 'ai_hub/Game.html', context)

def courses(request):
    return render(request, 'ai_hub/courses.html')

def events(request):
    meetups = Event.objects.all()
    upcoming = [event for event in meetups if event.is_upcoming()]
    if len(upcoming) == 0:
        upcoming = None 
    past = [event for event in meetups if not event.is_upcoming()]
    context = {'upcoming': upcoming, 'past': past[-2:]}
    return render(request, 'ai_hub/Events.html', context)

def meetups(request):
    meetups = Event.objects.all()
    context = {'meetups': meetups}
    return render(request, 'ai_hub/Meetups.html', context)

def about(request):
    team_members = Team.objects.all()
    context = {'team_members': team_members}
    return render(request, 'ai_hub/about.html', context)

def career_choice( request, pk ):
    section_content = CareerChoice.objects.filter(section=pk)
    categories = section_content.values_list('category', flat=True).distinct()
    selected_category = request.GET.get('category')
    if selected_category:
        section_content = section_content.filter(category=selected_category)

    context = {'pk': pk, 'categories': categories, 'selected_category': selected_category, 'data': section_content}
    return render(request, 'ai_hub/career_content.html', context)