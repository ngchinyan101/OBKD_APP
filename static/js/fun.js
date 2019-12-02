// bitcoin 

function buy() {
    $('#exampleModal').modal('show')
    var r = $("#bRate").text()
    $('#bValue').val(r)
}

$(document).ready(function () {
    $('#bInput').on('input', function() {
        var unit = parseFloat($('#bInput').val())
        var tr = parseFloat($('#bValue').val())
        console.log(unit + ' ' + tr)
        var re = $('#bresult').text('Value: ' + tr * unit)

    })
    var r = $("#bRate").val()
    console.log(r)
})

// litecoin 
function buylitecoin() {
    $('#exampleModal').modal('show')
    var r = $("#lRate").text()
    $('#lValue').val(r)
}

$(document).ready(function () {
    $('#lInput').on('input', function() {
        var unit = parseFloat($('#lInput').val())
        var tr = parseFloat($('#lValue').val())
        console.log(unit + ' ' + tr)
        var re = $('#lresult').text('Value: ' + tr * unit)
    })
    var r = $("#lRate").val()
    console.log(r)
})

// ethereum
function buyethereum() {
    $('#exampleModal').modal('show')
    var r = $("#eRate").text()
    $('#eValue').val(r)

}

$(document).ready(function () {
    $('#eInput').on('input', function() {
        var unit = parseFloat($('#eInput').val())
        var tr = parseFloat($('#eValue').val())
        console.log(unit + ' ' + tr)
        var re = $('#eresult').text('Value: ' + tr * unit)

    })
    var r = $("#eRate").val()
    console.log(r)
})