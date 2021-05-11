http://127.0.0.1:8000/api/patient/2/vaccine-center/?is_priority=false


function get_locations(url, tableTag){
    $.ajax({
        type: 'GET',
        contentType: "application/json; charset=utf-8",
        url: url,
        success: function (data) {
            console.log(data)


            for (var i = 0; i < data.length; i++) {
                $('#'+tableTag).DataTable().row.add( [
                    data[i].id,
                    data[i].name,
                    data[i].description,
                    '<a href="/work-orders/add/locations/'+data[i].id+'" class="view" title="" data-toggle="tooltip" data-original-title="View Details"><i class="material-icons"></i></a>'
                ] ).draw( false );
            }
        },
        error: function (a, jqXHR, exception) { }
    });
}