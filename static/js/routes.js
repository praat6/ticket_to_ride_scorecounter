function addRoute(n_train_cars, player_id)
{
    $.ajax({
        type: 'POST',
        url: '/counter/ajax/add-route/',
        data: {
            'n_train_cars': n_train_cars,
            'player_id': player_id,
            'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val(),
        },
        dataType: 'json',
    });
}

function removeRoute(n_train_cars, player_id)
{
    $.ajax({
        type: 'POST',
        url: '/counter/ajax/remove-route/',
        data: {
            'n_train_cars': n_train_cars,
            'player_id': player_id,
            'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val(),
        },
        dataType: 'json'
    });
}
