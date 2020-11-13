function update_routes_count_value(form_field_id, routes_count) {
    document.getElementById(form_field_id).value = routes_count
}

function addRoute(form_field_id, n_train_cars, player_id)
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
        success: function (data) {
            update_routes_count_value(form_field_id, data.routes_count)
        }
    });
}

function removeRoute(form_field_id, n_train_cars, player_id)
{
    $.ajax({
        type: 'POST',
        url: '/counter/ajax/remove-route/',
        data: {
            'n_train_cars': n_train_cars,
            'player_id': player_id,
            'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val(),
        },
        dataType: 'json',
        success: function (data) {
            update_routes_count_value(form_field_id, data.routes_count)
        }
    });
}
