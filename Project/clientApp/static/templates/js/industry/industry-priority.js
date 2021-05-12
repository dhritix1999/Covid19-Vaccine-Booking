$(document).ready(function () {

    get_industries('/api/industry/')


});


function get_industries(url){
    $.ajax({
        type: 'GET',
        contentType: "application/json; charset=utf-8",
        url: url,
        success: function (data) {
            console.log(data)

            for (var i = 0; i < data.length; i++) {
                $('#dataTable').DataTable().row.add( [
                    data[i].id,
                    data[i].name,
                    data[i].priority,
                        '<a href="industry/'+data[i].id+'/edit" class="edit"><i\n' +
                        '                                class="material-icons"\n' +
                        '                                title="Edit">&#xE254;</i></a>'+
                        '    <a  onclick="deleteEntity(&quot/api/industry/'+data[i].id+'&quot)" class="delete" style="cursor: pointer"><i\n' +
                        '                                class="material-icons"\n' +
                        '                                title="Delete">&#xe888;</i></a>'
                ] ).draw( false );
            }
        },
        error: function (a, jqXHR, exception) { }
    });
}