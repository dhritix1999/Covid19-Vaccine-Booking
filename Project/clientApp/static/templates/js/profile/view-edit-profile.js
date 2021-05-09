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

        patientForm.attr('action', '/api/patient/'+patient_id+'/')
        //update user form submission
        formSubmit(patientForm, false, 'Patient updated successfully', (form) => {

        return JSON.stringify({
            "email": $('#email').val(),
            "name": $('#name').val(),
            "gender": $('input[name="gender"]:checked').val(),
            "phone": $('#phone').val(),
            "password": $('#password').val(),
            "dateOfBirth": $('#dateOfBirth').val(),
            "emiratesID": $('#emiratesID').val(),
            "industry": $('#industry').val(),
            "locationLat": $('#locationLat').val(),
            "locationLng": $('#locationLng').val(),
            "determination": $('input[name="determination"]:checked').val(),
            "dosesTaken": $('#dosesTaken').val(),
            "patientMedicalIssues": $('#patientMedicalIssues').val(),
        });
    })

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
            $('#password').val(data.password)
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