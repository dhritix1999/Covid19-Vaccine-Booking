$(document).ready(function () {

    //validate admin
        validate_user('admin')
   const medicalIssueForm = $("#form");


   if (industryForm.attr('method') == 'POST')
       formSubmit(medicalIssueForm, true, 'Medicacl Issue added successfully');
   else {
       //fill up the form
       //get id value
       get_industry_by_id('/api/medical-issues/' + $("#id").val() + '/')
       formSubmit(medicalIssueForm, false, 'Medicacl Issue  updated successfully', (form) => {
           return JSON.stringify({
               "name": $('#name').val(),
               "vaccineEligibility": $('#vaccineEligibility').val(),
           });
       });
   }
});

function get_medical_issue_by_id(url) {
   $.ajax({
       type: 'GET',
       contentType: "application/json; charset=utf-8",
       url: url,
       success: function (data) {
           console.log(data)

           $('#name').val(data.name)
           $("#vaccineEligibility").prop("checked", data.vaccineEligibility);
       },
       error: function (a, jqXHR, exception) {
       }
   });
}

function myCheckBox() {
   var chkPrint = document.getElementById("vaccineEligibility");
   chkPrint.value = chkPrint.checked;
   console.log('value', chkPrint.value);
}