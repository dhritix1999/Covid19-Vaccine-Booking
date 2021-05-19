$(document).ready(function () {

 //validate admin
         validate_user('admin')
    get_industries('/api/vaccine-centers/')


});


function get_industries(url) {
    $.ajax({
        type: 'GET',
        contentType: "application/json; charset=utf-8",
        url: url,
        success: function (data) {
            console.log(data)

            for (var i = 0; i < data.length; i++) {
                $('#dataTable').DataTable().row.add([
                    data[i].id,
                    data[i].name,
                    ' <a href="https://www.google.com/maps/search/?api=1&query=' + data[i].locationLat + ',' + data[i].locationLng + '" target="_blank" title="Location"\n' +
                    '           class="location"><i class="material-icons md-30" style="color: darkblue">&#xe55f;</i></a>',
                    data[i].dosesPerHour,
                    data[i].dosesStock,
             '<a href="vaccine-centers/' + data[i].id + '/edit" class="edit"><i\n' +
                    '                                class="material-icons"\n' +
                    '                                title="Edit">&#xE254;</i></a>' +
             '<a data-url="/api/vaccine-centers/' + data[i].id+ '/"  onclick="deleteEntity(this.getAttribute(\'data-url\'))"   style="cursor: pointer" class="delete"><i\n' +
                                    ' class="material-icons" title="Delete">&#xe888;</i></a>'
                ]).draw(false);
            }
        },
        error: function (a, jqXHR, exception) {
        }
    });
}