

/**
 Convert Form to Json format
 **/
function convertFormToJSONString(form){
    var array = $(form).serializeArray();
    var json = {};

    jQuery.each(array, function() {
        json[this.name] = this.value || '';
    });

    return  JSON.stringify(json);

}

/**
 sample ajax delete
 **/
function deleteEntity(url, tag, tableTag = 'dataTable'){

    $.ajax({
        type: 'DELETE',
        url: url,
        success: function (data) {
            //print to log
            console.log('Deletion was successful.');
            console.log(data)

            // delete row
            $('#'+tableTag).DataTable().row('#'+tag).remove().draw();
        },
        error: function (data) {
            //print to log
            console.log('An error occurred.');
            console.log(data);

            //alert
            errorAlert(data);
        },
    });
}

/**
 sample ajax form handling
 **/
function formSubmit(form, formReset, successMessage, getFormData = convertFormToJSONString, redirectUrl = null) {

    form.submit(function (e) {
        e.preventDefault();
        e.stopPropagation();

        $.ajax({
            contentType: "application/json",
            type: form.attr('method'),
            url: form.attr('action'),
            data: getFormData(form),
            success: function (data) {

                if (redirectUrl != null){
                    window.location = redirectUrl;
                }
                // clear out the form
                if (formReset) form[0].reset();

                // print to log
                console.log('Submission was successful.');
                console.log(data)

                showalert(successMessage, "alert-success");
            },
            error: function (data) {
                //clear out the form
                form[0].reset();

                //print to log
                console.log('An error occurred.');
                console.log(data);

                //alert
                errorAlert(data.responseJSON.message)
            },
        });
    });
}

function setCookie(userType, id){

}