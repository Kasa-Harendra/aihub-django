from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('projects', views.projects, name='projects'),
    path('blogs', views.blogs, name='blogs'),
    path('about', views.about, name='about'),
    path('apps', views.apps, name='apps'),
    path('events', views.events, name='events'),
    path('career', views.career, name='career'),
    path('projects/games', views.games, name='games'),
    path('events/meetups', views.meetups, name='meetups'),
    path('blog_viewer/media/blogs/<str:pk>', views.blog_viewer, name='blog_viewers'),
]