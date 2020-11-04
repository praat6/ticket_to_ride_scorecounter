from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .forms import CreateGameForm
from .models import Game, Player


def create_game(request):
    form = CreateGameForm(request.POST)
    if form.is_valid():

        game = Game.objects.create()
        for hex_color_code, color_name in Player.COLOR_CHOICES:
            if player_name := form.data[color_name]:
                Player.objects.create(name=player_name, color=hex_color_code, game=game)

        return HttpResponseRedirect(reverse('game-detail', args=(game.code, )))

    return render(request, 'counter/index.html', {'form': form})


def game_detail(request, game_code):
    return HttpResponse(game_code)
