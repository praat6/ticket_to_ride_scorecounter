from django.db import models

from .helpers import gen_game_code, routes


class Game(models.Model):
    code = models.CharField(max_length=5, default=gen_game_code.generate)
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

    def score(self):
        return sum([route.to_score() for route in self.route_set.all()])

    def __str__(self):
        return '{} {}'.format(self.game.code, self.get_color_display())

    class Meta:
        unique_together = ('name', 'color', 'game')


class Route(models.Model):
    N_TRAIN_CARS_CHOICES = [
        (routes.one.n_train_cars, 'one'),
        (routes.two.n_train_cars, 'two'),
        (routes.three.n_train_cars, 'three'),
        (routes.four.n_train_cars, 'four'),
        (routes.five.n_train_cars, 'five'),
        (routes.six.n_train_cars, 'six')
    ]

    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    n_train_cars = models.IntegerField(choices=N_TRAIN_CARS_CHOICES)

    def to_score(self):
        for route_type in routes.types:
            if route_type.n_train_cars == self.n_train_cars:
                return route_type.score

        raise ValueError('Can\'t convert a route of {} train cars to a score.'.format(self.n_train_cars))
