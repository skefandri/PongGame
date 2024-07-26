from django.shortcuts import render

# Create your views here.
def game_selection(request):
    return render(request, 'game/game_selection.html')


def home(request):
    return render(request, 'game/home.html')
