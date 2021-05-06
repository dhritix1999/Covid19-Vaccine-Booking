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
    formSubmit(patientForm, false, 'Patient registered successfully', convertFormToJSONString, '/')
});

function loadIndustries(url) {
    $.ajax({
        type: 'GET',
        contentType: "application/json; charset=utf-8",
        url: url,
        success: function (data) {
            console.log(data)
            for (var i = 0; i < data.length; i++) {
                var value = data[i].name;
                $("#industry").append("<option value='" + value + "'>" + value + "</option>");
            }
        },
        error: function (data) {
            console.log(data)
        },
    });
}

function loadMedicalIssues(url){
       $.ajax({
        type: 'GET',
        contentType: "application/json; charset=utf-8",
        url: url,
        success: function (data) {
            console.log(data)
            for (var i = 0; i < data.length; i++) {
                var value = data[i].name;
                $("#patientMedicalIssues").append("<option value='" + value + "'>" + value + "</option>");
            }
             $('.selectpicker').selectpicker('refresh');
        },
        error: function (data) {
            console.log(data)
        },
    });
}