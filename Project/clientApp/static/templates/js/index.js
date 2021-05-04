$(document).ready(function () {
  const adminSignInButton = document.getElementById('adminSignIn');
const patientSignInButton = document.getElementById('patientSignIn');
const container = document.getElementById('container');

adminSignInButton.addEventListener('click', () => {
	container.classList.add("right-panel-active");
});

patientSignInButton.addEventListener('click', () => {
	container.classList.remove("right-panel-active");
});

    const patientForm = $("#patientForm");

    indexFormSubmit(patientForm, '/patient');

    const adminForm = $("#adminForm");
     indexFormSubmit(adminForm, '/admins');
});


function indexFormSubmit(form, redirectUrl = null, getFormData = convertFormToJSONString) {

    form.submit(function (e) {
        e.preventDefault();
        e.stopPropagation();

        $.ajax({
            contentType: "application/json",
            type: form.attr('method'),
            url: form.attr('action'),
            data: getFormData(form),
            success: function (data) {

                 console.log(data);

                if (redirectUrl == '/patient'){
                    document.cookie = "patient="+data.id
                    window.location = redirectUrl;
                }
                else if (redirectUrl == '/admins'){
                    document.cookie = "admin="+data.id
                      window.location = redirectUrl;
                }

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