from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.create_game, name='create-game'),
    path('<str:game_code>/', views.game_detail, name='game-detail'),
    url(r'^ajax/add-route/$', views.add_route, name='add-route'),
    url(r'^ajax/subtract-route/$', views.subtract_route, name='subtract-route')
]
