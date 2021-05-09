/**
 Bootstrap Alerts -
 Function Name - showalert()
 Inputs - message,alerttype
 Example - showalert("Invalid Login","alert-error")
 Types of alerts -- "alert-error","alert-success","alert-info","alert-warning"
 Required - You only need to add a alert_placeholder div in your html page wherever you want to display these alerts "<div id="alert_placeholder"></div>"
 Written On - 14-Jun-2013
 **/
function showalert(message,alerttype) {

    $('#alert_placeholder').append('<div id="alertdiv" class="alert ' +  alerttype + '"><a class="close" data-dismiss="alert">×</a><span>'+message+'</span></div>')
    setTimeout(function() { // this will automatically close the alert and remove this if the locations doesnt close it in 5 secs
        $("#alertdiv").remove();
    }, 5000);
}

/**
 Use this whenever we need to output error from JSONResponse
 **/
function errorAlert(message){
    if (message == null){
        showalert("An Error Occurred, Try Again", "alert-danger");
    }
    else{
        showalert(message, "alert-danger");
    }
}

/**
 *  Convert form to JSON format
 *
 * @param form object
 * @return JSON.stringify(form)
 * */
function convertFormToJSONString(form) {
    var array = $(form).serializeArray();
    var json = {};

    jQuery.each(array, function () {
        json[this.name] = this.value || '';
    });

    console.log(JSON.stringify(json))
    return JSON.stringify(json);

}



/**
 *  Delete row in a table
 *
 * @param url of DELETE api
 * @param tag id of the table row
 * @param tableTag the id of the table
 * */
function deleteEntity(url, tag, tableTag = 'dataTable') {

    $.ajax({
        type: 'DELETE',
        url: url,
        success: function (data) {
            //print to log
            console.log('Deletion was successful.');
            console.log(data)

            // delete row
            $('#' + tableTag).DataTable().row('#' + tag).remove().draw();
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
function formSubmit(form, formReset, successMessage, getFormData = convertFormToJSONString, redirectUrl = null, sessionMessage = null) {

    form.submit(function (e) {
        e.preventDefault();
        e.stopPropagation();

        $.ajax({
            contentType: "application/json",
            type: form.attr('method'),
            url: form.attr('action'),
            data: getFormData(form),
            success: function (data) {

                showalert(successMessage, "alert-success");

                if (redirectUrl != null) {
                    if (sessionMessage != null)
                        sessionStorage.setItem("message", sessionMessage);
                    window.location = redirectUrl;
                }
                // clear out the form
                if (formReset) form[0].reset();

                // print to log
                console.log('Submission was successful.');
                console.log(data)
            },
            error: function (data) {
                //clear out the form
                form[0].reset();

                //print to log
                console.log('An error occurred.');
                console.log(data);

                //alert
                for (x in data.responseJSON){
                    errorAlert(data.responseJSON[x])
                }

            },
        });
    });
}

/**
 * @param url of the GET api
 * @returns data of the ajax get
 * */
function getDataFromUrl(url) {
    $.ajax({
        type: 'GET',
        contentType: "application/json; charset=utf-8",
        url: url,
        success: function (data) {
            console.log(data)
            return data
        },
        error: function (data) {
            console.log(data)
            return 'error'
        },
    });
}



//Get cookie routine by Shelley Powers
function get_cookie(Name) {
  var search = Name + "="
  var returnvalue = "";
  if (document.cookie.length > 0) {
    offset = document.cookie.indexOf(search)
    // if cookie exists
    if (offset != -1) {
      offset += search.length
      // set index of beginning of value
      end = document.cookie.indexOf(";", offset);
      // set index of end of cookie value
      if (end == -1) end = document.cookie.length;
      returnvalue=unescape(document.cookie.substring(offset, end))
      }
   }
  return returnvalue;
}