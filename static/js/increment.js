function incrementValue(element_id)
{
    var value = parseInt(document.getElementById(element_id).value, 10);
    value = isNaN(value) ? 0 : value;
    value++;
    document.getElementById(element_id).value = value;
}

function decrementValue(element_id)
{
    var value = parseInt(document.getElementById(element_id).value, 10);
    value = isNaN(value) ? 0 : value;
    value--;
    document.getElementById(element_id).value = value;

    $.ajax({
        url: '/counter/ajax/add/',
        data: {'value': value},
        dataType: 'json'
    })
}
