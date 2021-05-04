

/**
 *  Convert form to JSON format
 *
 * @param form object
 * @return JSON.stringify(form)
 * */
function convertFormToJSONString(form){
    var array = $(form).serializeArray();
    var json = {};

    jQuery.each(array, function() {
        json[this.name] = this.value || '';
    });

    return  JSON.stringify(json);

}

/**
 *  Delete row in a table
 *
 * @param url of DELETE api
 * @param tag id of the table row
 * @param tableTag the id of the table
 * */
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
 *  Submits a form
 *
 * @param form object
 * @param formReset true if you want the form to be cleared out
 * @param successMessage what the alert message should display
 * @param getFormData getting the form data in json format
 * @param redirectUrl redirection url after form submission
 * */
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

/**
 * @param url of the GET api
 * @returns data of the ajax get
 * */
function getDataFromUrl(url){
     $.ajax({
            contentType: "application/json",
            type: 'GET',
            url: url,
            success: function (data) {

                return data
            },
            error: function (data) {

                return 'error'
            },
        });
}