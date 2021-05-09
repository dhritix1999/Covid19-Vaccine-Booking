$(document).ready(function () {

    //get cookie
    console.log(get_cookie('patient'))
    patient_id = get_cookie('patient')

    $('.selectpicker').selectpicker();

    if (patient_id != '') {

        $("#industry").empty()
        $("#patientMedicalIssues").empty()

        $.when(
            //get industries
            loadIndustries('/api/industry/'),

            //get medical problems
            loadMedicalIssues('/api/medical-issue/')
        ).then(function () {
            loadUserDetails('/api/patient/' + patient_id + '/')
        })


        // user form
        const patientForm = $("#form");

        //get user data and populate form

    }
})
;


function loadUserDetails(url) {

    $.ajax({
        type: 'GET',
        contentType: "application/json; charset=utf-8",
        url: url,
        success: function (data) {
            console.log(data)

            $('#email').val(data.email)
            $('#name').val(data.name)
            $('#gender').val(data.gender)
            $('#phone').val(data.phone)
            $('#dateOfBirth').val(data.dateOfBirth)
            $('#emiratesID').val(data.emiratesID)
            $('#industry').val(data.industry)
            $('#locationLat').val(data.locationLat)
            $('#locationLng').val(data.locationLng)
            $('#determination').val(data.determination)
            $('#dosesTaken').val(data.dosesTaken)
            $('#patientMedicalIssues').val(data.patientMedicalIssues)
               $('.selectpicker').selectpicker('refresh');

        },
        error: function (data) {
            console.log(data)
        },
    });
}


function loadIndustries(url) {
    $.ajax({
        type: 'GET',
        contentType: "application/json; charset=utf-8",
        url: url,
        success: function (data) {
            console.log(data)
            for (var i = 0; i < data.length; i++) {
                $("#industry").append("<option value='" + data[i].id + "'>" + data[i].name + "</option>");
            }
        },
        error: function (data) {
            console.log(data)
        },
    });
}

function loadMedicalIssues(url) {
    $.ajax({
        type: 'GET',
        contentType: "application/json; charset=utf-8",
        url: url,
        success: function (data) {
            console.log(data)
            for (var i = 0; i < data.length; i++) {
                $("#patientMedicalIssues").append("<option value='" + data[i].id + "'>" + data[i].name + "</option>");
            }
             $('.selectpicker').selectpicker('refresh');
        },
        error: function (data) {
            console.log(data)
        },
    });
}