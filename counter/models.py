from django.db import models
from colorfield.fields import ColorField

from .settings import game_code_gen


class Game(models.Model):
    code = models.CharField(max_length=5, default=game_code_gen)
    datetime = models.DateTimeField(auto_now=True)


class Player(models.Model):
    RED = '#e93b23'
    BLUE = '#256881'
    YELLOW = '#e9bd2c'
    GREEN = '#196337'
    BLACK = '#171207'

    COLORS = [('Red', RED), ('Blue', BLUE), ('Yellow', YELLOW), ('Green', GREEN), ('Black', BLACK)]

    name = models.CharField(max_length=20)
    color = ColorField(choices=COLORS)
    score = models.IntegerField(default=0)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('name', 'color', 'game')
