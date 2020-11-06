function incrementValue(element_id)
{
    let value = parseInt(document.getElementById(element_id).value, 10);
    value = isNaN(value) ? 0 : value;
    value++;
    document.getElementById(element_id).value = value;

    $.ajax({
        url: '/counter/ajax/add-route/',
        data: {'value': value},
        dataType: 'json'
    })
}

function decrementValue(element_id)
{
    let value = parseInt(document.getElementById(element_id).value, 10);
    value = isNaN(value) ? 0 : value;
    value--;
    document.getElementById(element_id).value = value;

    $.ajax({
        url: '/counter/ajax/subtract-route/',
        data: {'value': value},
        dataType: 'json'
    })
}
