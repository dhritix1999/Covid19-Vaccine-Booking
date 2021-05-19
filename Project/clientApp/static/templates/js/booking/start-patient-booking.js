let patient_id
$(document).ready(function () {

     validate_user('patient')
    patient_id = get_cookie('patient')
    console.log(patient_id)

    $("#vaccineEligibility").click(function (e) {

        checkVaccineEligibility().then(function (eligible) {
            if (eligible) {
                //show Proceed booking button
                document.getElementById('proceedBooking').style.visibility = 'visible';
                //pop up modal with link to next step
                $('#trueModalCenter').modal('show')

            } else {
                //pop up modal with not eligible message

                $('#falseModalCenter').modal('show')
            }
        });
    });
});

function checkVaccineEligibility() {
    return new Promise(function (resolve, reject) {
        $.ajax({
            type: 'GET',
            contentType: "application/json; charset=utf-8",
            url: '/api/patients/' + patient_id + '/medical-issues',
            success: function (data) {
                console.log(data)
                let eligible = true
                for (var i = 0; i < data.length; i++) {
                    if (!data[i].vaccineEligibility) {
                        eligible = false
                    }
                }
                resolve(eligible)
            },
            error: function (data) {
                reject(data)
            },
        });
    })

}