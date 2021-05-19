let patient_id
bookings = []
$(document).ready(function () {


    $.when(
          //validate user first
     validate_user('patient'),
        patient_id = get_cookie('patient'),
    ).then(function () {
        get_bookings('/api/patients/' + patient_id + '/booking-slots/')
    })

});

function get_bookings(url) {
    $.ajax({
        type: 'GET',
        contentType: "application/json; charset=utf-8",
        url: url,
        success: function (data) {
            console.log(data)
            let newRow;
            for (var i = 0; i < data.length; i++) {

                newRow = new Object()
                newRow.id = data[i].id
                newRow.bookingSlotID = data[i].bookingSlotID

                $.ajax({
                    type: 'GET',
                    contentType: "application/json; charset=utf-8",
                    url: '/api/booking-slots/' + newRow.bookingSlotID + '/',
                    success: function (slots) {
                        console.log(slots)
                        newRow.timeSlot = slots.timeSlot

                        //get vaccine centers details
                        $.ajax({
                            type: 'GET',
                            contentType: "application/json; charset=utf-8",
                            url: '/api/vaccine-centers/' + slots.centerID,
                            success: function (vaccineCenters) {
                                console.log(vaccineCenters)

                                newRow.vaccineCenter = vaccineCenters.name
                                newRow.locationLat = vaccineCenters.locationLat
                                newRow.locationLng = vaccineCenters.locationLng

                                //add new row to array
                                bookings.push(newRow)

                            },
                            error: function (a, jqXHR, exception) {
                            }
                        }).done(function (data) {

                            console.log('bookings')
                            console.log(bookings)
                            //append objects to table
                            for (var i = 0; i < bookings.length; i++) {
                                $('#dataTable').DataTable().row.add([
                                    bookings[i].id,
                                    bookings[i].vaccineCenter,
                                    ' <a href="https://www.google.com/maps/search/?api=1&query=' + bookings[i].locationLat + ',' + bookings[i].locationLng + '" target="_blank" title="Location"\n' +
                                    '           class="location"><i class="material-icons md-30" style="color: darkblue">&#xe55f;</i></a>',
                                    bookings[i].timeSlot,
                                    'Upcoming',
                                    '   <a data-url="/api/patients/' + patient_id + '/booking-slots/' + bookings[i].bookingSlotID + '/"  onclick="deleteEntity(this.getAttribute(\'data-url\'))"   style="cursor: pointer" class="delete"><i\n' +
                                    ' class="material-icons" title="Delete Booking">&#xe888;</i></a>'
                                ]).draw(false);
                            }
                        });

                    },
                    error: function (a, jqXHR, exception) {
                    }
                });
            }
        },
        error: function (a, jqXHR, exception) {
        }
    });
}