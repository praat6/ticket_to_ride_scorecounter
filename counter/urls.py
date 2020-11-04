from django.urls import path

from . import views

urlpatterns = [
    path('', views.create_game, name='create-game'),
    path('<str:game_code>/', views.game_detail, name='game-detail')
]
