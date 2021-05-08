$(document).ready(function () {

    // multi select list drop down
    $('.selectpicker').selectpicker();

    //get industries
    $("#industry").empty()
    loadIndustries('/api/industry/')

    //get medical problems
    $("#patientMedicalIssues").empty()
    loadMedicalIssues('/api/medical-issue/')

    //register form
    const patientForm = $("#form");

    //form submission
    formSubmit(patientForm, true, 'Patient registered successfully', (form) => {

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
});

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