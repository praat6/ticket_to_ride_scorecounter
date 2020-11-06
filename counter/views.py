from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from .forms import CreateGameForm
from .models import Game, Player, Route


def create_game(request):
    form = CreateGameForm(request.POST)
    if form.is_valid():

        game = Game.objects.create()
        for hex_color_code, color_name in Player.COLOR_CHOICES:
            if player_name := form.data[color_name]:
                Player.objects.create(name=player_name, color=hex_color_code, game=game)

        return HttpResponseRedirect(reverse('game-detail', args=(game, )))

    return render(request, 'counter/index.html', {'form': form})


def game_detail(request, game_code):
    players = Game.objects.get(code=game_code).player_set.all()
    return render(request, 'counter/game.html', {'players': players, 'n_train_car_choices': Route.N_TRAIN_CARS_CHOICES})


def add_score(request):
    score = request.GET.get('value', None)
    print(score)
    return JsonResponse({'score': score})
