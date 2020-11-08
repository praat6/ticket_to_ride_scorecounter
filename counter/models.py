from django.db import models

from .settings import game_code_gen


class Game(models.Model):
    code = models.CharField(max_length=5, default=game_code_gen)
    datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.code


class Player(models.Model):
    RED = '#e93b23'
    BLUE = '#256881'
    YELLOW = '#e9bd2c'
    GREEN = '#196337'
    BLACK = '#171207'

    COLOR_CHOICES = [(RED, 'red'), (BLUE, 'blue'), (YELLOW, 'yellow'), (GREEN, 'green'), (BLACK, 'black')]

    name = models.CharField(max_length=20)
    color = models.CharField(max_length=7, choices=COLOR_CHOICES)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    def get_n_routes(self, n_train_cars):
        return self.route_set.filter(n_train_cars=n_train_cars).count()

    def __str__(self):
        return '{} {}'.format(self.game.code, self.get_color_display())

    class Meta:
        unique_together = ('name', 'color', 'game')


class Route(models.Model):
    ONE_TRAIN_CAR = 1
    TWO_TRAIN_CARS = 2
    THREE_TRAIN_CARS = 3
    FOUR_TRAIN_CARS = 4
    FIVE_TRAIN_CARS = 5
    SIX_TRAIN_CARS = 6

    N_TRAIN_CARS_CHOICES = [(ONE_TRAIN_CAR, 'one'), (TWO_TRAIN_CARS, 'two'), (THREE_TRAIN_CARS, 'three'),
                            (FOUR_TRAIN_CARS, 'four'), (FIVE_TRAIN_CARS, 'five'), (SIX_TRAIN_CARS, 'six')]

    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    n_train_cars = models.IntegerField(choices=N_TRAIN_CARS_CHOICES)
