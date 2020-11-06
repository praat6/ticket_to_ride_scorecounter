from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.create_game, name='create-game'),
    path('<str:game_code>/', views.game_detail, name='game-detail'),
    url(r'/ajax/add/', views.add_score, name='add-score')
]
