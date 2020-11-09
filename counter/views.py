from collections import defaultdict

from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse

from .forms import CreateGameForm, ModifyRouteForm
from .models import Game, Player, Route
from .helpers import routes


def create_game(request):
    form = CreateGameForm(request.POST)

    if form.is_valid():
        game = Game.objects.create()
        for hex_color_code, color_name in Player.COLOR_CHOICES:
            if player_name := form.data[color_name]:
                game.player_set.create(name=player_name, color=hex_color_code)

        return HttpResponseRedirect(reverse('game-detail', args=(game, )))

    return render(request, 'counter/index.html', {'form': form})


def game_detail(request, game_code):
    players = Game.objects.get(code=game_code).player_set.all()

    forms = defaultdict(list)
    for player in players:
        for route_type in routes.types:
            forms[player].append(ModifyRouteForm(player=player, route_type=route_type))

    return render(request, 'counter/game.html', {'player_forms': dict(forms)})


def add_route(request):
    player_route_set = Player.objects.get(id=request.POST.get('player_id')).route_set
    player_route_set.create(n_train_cars=request.POST.get('n_train_cars'))

    return JsonResponse({'n_routes': player_route_set.count()})


def remove_route(request):
    player_route_set = Player.objects.get(id=request.POST.get('player_id')).route_set
    player_route_set.filter(n_train_cars=request.POST.get('n_train_cars')).last().delete()

    return JsonResponse({'n_routes': player_route_set.count()})
