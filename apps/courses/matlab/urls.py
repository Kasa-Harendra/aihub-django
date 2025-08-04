from django.urls import path
from . import views

app_name = 'matlab'

urlpatterns = [
    path('', views.landing, name="landing"),
    path("index/", views.index, name="index"),
    path('experiment_desc/', views.exp_detail, name="experiment_detail"),
    path('experiment_view/', views.exp_view, name="experiment_viewer")
]
