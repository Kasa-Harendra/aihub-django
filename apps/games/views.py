from django.shortcuts import render

# Create your views here.
def play_game(request, id):
    return render(request, f'games/{id}.html')