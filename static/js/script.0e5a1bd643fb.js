$(function () {
    var $myForm = $('.my-ajax-form')
    var $myTable = $('.table')
    $myForm.submit(function (event) {
        event.preventDefault()
        var $formData = $(this).serialize()
        var $thisURL = $myForm.attr('data-url')
        $.ajax({
            method: "POST",
            url: $thisURL,
            data: $formData,
            success: function () {
                $myForm.trigger('reset')
                $myTable.load($thisURL + ' .table')
            },
        })
    })
})