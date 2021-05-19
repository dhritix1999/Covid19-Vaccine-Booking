let patient_id
$(document).ready(function () {

    $.when(
        validate_user('patient'),
        patient_id = get_cookie('patient'),
    ).then(function () {
        get_vaccine_centres('/api/patients/' + patient_id + '/vaccine-centers/?is_priority=true')
    })

});

function get_vaccine_centres(url) {
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
                    '   <a href="/patient/booking/vaccine-center/'+data[i].id+'/slots" title="Proceed" class="next"><i\n' +
                    '            class="material-icons md-30" style="color:#e12454;">&#xe5c8;</i></a>'
                ]).draw(false);
            }
        },
        error: function (a, jqXHR, exception) {
        }
    });
}