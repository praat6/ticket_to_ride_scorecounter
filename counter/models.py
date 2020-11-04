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
    score = models.IntegerField(default=0)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    def __str__(self):
        return '{} {}'.format(self.game.code, self.get_color_display())

    class Meta:
        unique_together = ('name', 'color', 'game')
