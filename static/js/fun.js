// function displayBitcoin() {
//     var bRate = parseFloat($('#bRate').val())
//     var rate = bRate * Number.parseFloat(document.querySelector("#inputAmt").value);
//     if (rate > 500.0) {
//         window.alert("You cannot transfer more than SGD$500");
//         document.querySelector("#result").style = "visibility:visible;";
//         document.querySelector("#inputAmt").value = 500 / {{bRate}};
//         document.querySelector("#inputPassword3").value = 500;
//         return;
//     }
//     document.querySelector("#result").style = "visibility:visible;";
//     document.querySelector("#inputPassword3").value = rate;
// }


// // bitcoin 

function buy() {
    $('#exampleModal').modal('show')
    var r = $("#bitcoinRate").text()
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

function buysilver() {
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

// crude oil

function crudeoil() {
    $('#exampleModal').modal('show')
    var r = $("#cRate").text()
    $('#cValue').val(r)

}

$(document).ready(function () {
    $('#cInput').on('input', function() {
        var unit = parseFloat($('#cInput').val())
        var tr = parseFloat($('#cValue').val())
        console.log(unit + ' ' + tr)
        var re = $('#cresult').text('Value: ' + tr * unit)

    })
    var r = $("#cRate").val()
    console.log(r)
})

// dbs 
function dbs() {
    $('#exampleModal').modal('show')
    var r = $("#dbsRate").text()
    $('#dbsValue').val(r)

}

$(document).ready(function () {
    $('#dbsInput').on('input', function() {
        var unit = parseFloat($('#dbsInput').val())
        var tr = parseFloat($('#dbsValue').val())
        console.log(unit + ' ' + tr)
        var re = $('#dbsresult').text('Value: ' + tr * unit)

    })
    var r = $("#dbsRate").val()
    console.log(r)
})

// ocbc
function ocbc() {
    $('#exampleModal').modal('show')
    var r = $("#ocbcRate").text()
    $('#ocbcValue').val(r)

}

$(document).ready(function () {
    $('#ocbcInput').on('input', function() {
        var unit = parseFloat($('#ocbcInput').val())
        var tr = parseFloat($('#ocbcValue').val())
        console.log(unit + ' ' + tr)
        var re = $('#ocbcresult').text('Value: ' + tr * unit)

    })
    var r = $("#ocbcRate").val()
    console.log(r)
})

// uob
function uob() {
    $('#exampleModal').modal('show')
    var r = $("#uobRate").text()
    $('#uobValue').val(r)

}

$(document).ready(function () {
    $('#uobInput').on('input', function() {
        var unit = parseFloat($('#uobInput').val())
        var tr = parseFloat($('#uobValue').val())
        console.log(unit + ' ' + tr)
        var re = $('#uobresult').text('Value: ' + tr * unit)

    })
    var r = $("#uobRate").val()
    console.log(r)
})

// cad/sgd
function cad() {
    $('#exampleModal').modal('show')
    var r = $("#cadRate").text()
    $('#cadValue').val(r)

}

$(document).ready(function () {
    $('#cadInput').on('input', function() {
        var unit = parseFloat($('#cadInput').val())
        var tr = parseFloat($('#cadValue').val())
        console.log(unit + ' ' + tr)
        var re = $('#cadresult').text('Value: ' + tr * unit)

    })
    var r = $("#cadRate").val()
    console.log(r)
})

// jpy/sgd
function jpy() {
    $('#exampleModal').modal('show')
    var r = $("#jpyRate").text()
    $('#jpyValue').val(r)

}

$(document).ready(function () {
    $('#jpyInput').on('input', function() {
        var unit = parseFloat($('#jpyInput').val())
        var tr = parseFloat($('#jpyValue').val())
        console.log(unit + ' ' + tr)
        var re = $('#jpyresult').text('Value: ' + tr * unit)

    })
    var r = $("#jpyRate").val()
    console.log(r)
})

// usd/sgd
function usd() {
    $('#exampleModal').modal('show')
    var r = $("#usdRate").text()
    $('#usdValue').val(r)

}

$(document).ready(function () {
    $('#usdInput').on('input', function() {
        var unit = parseFloat($('#usdInput').val())
        var tr = parseFloat($('#usdValue').val())
        console.log(unit + ' ' + tr)
        var re = $('#usdresult').text('Value: ' + tr * unit)

    })
    var r = $("#usdRate").val()
    console.log(r)
})