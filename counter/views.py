from django.shortcuts import render
from django.http import HttpResponse
from .forms import CreateGameForm
from .models import Game, Player


def create_game(request):
    form = CreateGameForm(request.POST)

    if form.is_valid():
        game = Game.objects.create()
        return HttpResponse(game.code)

    return render(request, 'counter/index.html', {'form': form})
