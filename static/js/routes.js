function getRoutesCount(element) {
    let routes_count_parent = element.parentElement;
    return routes_count_parent.querySelector('[name=routes_count]')
}

function getPlayerScore(element) {
    let player_div = element.parentElement.parentElement.parentElement;
    return player_div.querySelector('[name=player-score]')
}

function addRoute(n_train_cars, player_id, element)
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
            let routes_count = getRoutesCount(element);
            routes_count.value = data.routes_count;

            let player_score = getPlayerScore(element);
            player_score.value = data.player_score;
        }
    });
}

function removeRoute(n_train_cars, player_id, element)
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
            let routes_count = getRoutesCount(element);
            routes_count.value = data.routes_count;

            let player_score = getPlayerScore(element);
            player_score.value = data.player_score;
        }
    });
}
