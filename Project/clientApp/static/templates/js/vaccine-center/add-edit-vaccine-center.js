$(document).ready(function () {

        //validate admin
         validate_user('admin')
    const vaccineCenterForm = $("#form");

    if (vaccineCenterForm.attr('method') == 'POST')
        formSubmit(vaccineCenterForm, true, 'Vaccine Center added successfully');
    else {
        //fill up the form
        //get id value
        get_vaccine_center_by_id('/api/vaccine-centers/' + $("#id").val() + '/')
        formSubmit(vaccineCenterForm, false, 'Vaccine Center updated successfully');
    }
});

function get_vaccine_center_by_id(url) {
    $.ajax({
        type: 'GET',
        contentType: "application/json; charset=utf-8",
        url: url,
        success: function (data) {
            console.log(data)

            $('#name').val(data.name)
            $('#locationLat').val(data.locationLat)
            $('#locationLng').val(data.locationLng)
            $('#dosesStock').val(data.dosesStock)
            $('#dosesPerHour').val(data.dosesPerHour)

        },
        error: function (a, jqXHR, exception) {
        }
    });
}
