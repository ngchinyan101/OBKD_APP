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

// gold

function buygold() {
    $('#exampleModal').modal('show')
    var r = $("#gRate").text()
    $('#gValue').val(r)

}

$(document).ready(function () {
    $('#eInput').on('input', function() {
        var unit = parseFloat($('#gInput').val())
        var tr = parseFloat($('#gValue').val())
        console.log(unit + ' ' + tr)
        var re = $('#gResult').text('Value: ' + tr * unit)

    })
    var r = $("#gRate").val()
    console.log(r)
})

// silver

function buygold() {
    $('#exampleModal').modal('show')
    var r = $("#sRate").text()
    $('#sValue').val(r)

}

$(document).ready(function () {
    $('#sInput').on('input', function() {
        var unit = parseFloat($('#sInput').val())
        var tr = parseFloat($('#sValue').val())
        console.log(unit + ' ' + tr)
        var re = $('#sResult').text('Value: ' + tr * unit)

    })
    var r = $("#sRate").val()
    console.log(r)
})
