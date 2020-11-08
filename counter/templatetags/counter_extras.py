from django import template


register = template.Library()


@register.simple_tag
def get_n_routes(player, n_train_cars):
    return player.get_n_routes(n_train_cars)
