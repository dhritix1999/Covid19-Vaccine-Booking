$(document).ready(function () {

     //validate admin
         validate_user('admin')
    const industryForm = $("#form");

    if (industryForm.attr('method') == 'POST')
        formSubmit(industryForm, true, 'Industry added successfully');
    else {
        //fill up the form
        //get id value
        get_industry_by_id('/api/industries/' + $("#id").val() + '/')
        formSubmit(industryForm, false, 'Industry updated successfully', (form) => {
            return JSON.stringify({
                "name": $('#name').val(),
                "priority": $('#priority').val(),
            });
        });
    }
});

function get_industry_by_id(url) {
    $.ajax({
        type: 'GET',
        contentType: "application/json; charset=utf-8",
        url: url,
        success: function (data) {
            console.log(data)

            $('#name').val(data.name)
            $("#priority").prop("checked", data.priority);
        },
        error: function (a, jqXHR, exception) {
        }
    });
}

function myCheckBox() {
    var chkPrint = document.getElementById("priority");
    chkPrint.value = chkPrint.checked;
    console.log('value', chkPrint.value);
}