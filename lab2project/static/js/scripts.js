/**
 * Created by Narvis Gil on 30/10/2016.
 */
$(document).ready(function () {
    $('#btnBuscar').click(function () {
        $.ajax(
            {url:'/cita/buscar/20923179',
        success:function (data) {
            $('#nombrePaciente').html(data);
        }
        })
    })
})