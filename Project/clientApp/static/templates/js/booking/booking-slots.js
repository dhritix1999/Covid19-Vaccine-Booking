let patient_id, vaccine_center_id;
$(document).ready(function () {

    //validate user first
     validate_user('patient')


    patient_id = get_cookie('patient');
    vaccine_center_id = $('#vaccineCenter').val()

    //inistiaize table
    const table = $('#dataTable').DataTable({
        searching: false,
        paging: false,
        bInfo: false
    });

    //initialize date for date picker
    document.getElementById('bookingOn').valueAsDate = new Date();


    //initialize booking slots
    add_booking_slots()

});

function add_booking_slots() {
    let counter = 1
    for (var i = 9; i < 19; i++) {
        $('#dataTable').DataTable().row.add([
            i + ':00 - ' + i + ':59',
            `<button class='btn btn-main btn-round-full' data-id='${(() => {
                const d = new Date();
                d.setUTCHours(i, 0, 0, 0)
                return d.toISOString().slice(10, 19);
            })()}\' onclick="check_booking(this.getAttribute('data-id'))" style='padding: 6pt 12pt;'>Book</button>`
        ]).draw(false);
    }

}

function check_booking(time) {
    var timeSlot = $('#bookingOn').val() + '' + time

    base_url = '/api/patients/' + patient_id + '/vaccine-centers/' + vaccine_center_id + '/booking-slots/'

    $.ajax({
        type: 'GET',
        contentType: "application/json; charset=utf-8",
        url: base_url + '?is_available=false&filtered_date=' + timeSlot,
        success: function (data) {
            console.log(data)

            //check if it is an empty list
            //if empty means user can book
            if (data.length == 0) {

                $.ajax({
                    type: 'GET',
                    contentType: "application/json; charset=utf-8",
                    url: base_url + '?is_available=true&filtered_date=' + timeSlot,
                    success: function (data) {
                        console.log(data)

                        //check if there is an existing slot
                        if (data.length == 0) {
                            //create a new booking slot
                            create_new_booking_slot_and_book(timeSlot)
                        } else {
                            //book the time slot
                            book_an_appointement(data.id, data.timeSlot)
                        }
                    },
                    error: function (data) {
                        showalert('System Error! Please try again later', 'alert-danger')
                    },
                });
            } else {
                //show modal that user cant book
                $('#cantBook').modal('show')
            }
        },
        error: function (a, jqXHR, exception) {
            showalert('System Error! Please try again later', 'alert-danger')

        }
    });

}

function create_new_booking_slot_and_book(timeSlot) {

    $.ajax({
        contentType: "application/json",
        type: 'POST',
        url: '/api/booking-slots/',
        data: JSON.stringify({
            "centerID": vaccine_center_id,
            "timeSlot": timeSlot + 'Z'
        }),
        success: function (data) {
            // print to log
            console.log('Submission was successful.');
            console.log(data)

            book_an_appointement(data.id, data.timeSlot)
        },
        error: function (data) {},
    });
}

function book_an_appointement(slot_id, time) {
    $.ajax({
        contentType: "application/json",
        type: 'POST',
        url: '/api/patients/' + patient_id + '/booking-slots/' + slot_id + '/',
        success: function (data) {
            // print to log
            console.log('Submission was successful.');
            console.log(data)

              $(".modal-body #bookTime").val( time );
              $('#successBook').modal('show')
        },
        error: function (data) {

        },
    });
}

