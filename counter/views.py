from collections import defaultdict

from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse

from .forms import CreateGameForm, RoutesForm
from .models import Game, Player
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
            forms[player].append(RoutesForm(player=player, n_train_cars=route_type.n_train_cars))

    return render(request, 'counter/game.html', {'player_forms': dict(forms)})


def get_player_route_set(player_id):
    return Player.objects.get(id=player_id).route_set


def add_route(request):
    player_route_set = Player.objects.get(id=request.POST.get('player_id')).route_set
    player_route_set.create(n_train_cars=(n_train_cars := request.POST.get('n_train_cars')))

    return JsonResponse({'routes_count': player_route_set.filter(n_train_cars=n_train_cars).count()})


def remove_route(request):
    player = Player.objects.get(id=request.POST.get('player_id'))
    player_routes = player.route_set.filter(n_train_cars=request.POST.get('n_train_cars'))
    player_routes.last().delete()

    return JsonResponse({'routes_count': player_routes.count()})
