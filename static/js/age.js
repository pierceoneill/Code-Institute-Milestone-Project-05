$(function() {
    $('input[name="dob"]').daterangepicker({
        singleDatePicker: true,
        showDropdowns: true
    }, 
    function(start, end, label) {
        var years = moment().diff(start, 'years');
        $("#age").val("You are " + years + " years old.");
    });
});
