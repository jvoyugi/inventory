
$(function () {
    var $myForm = $('.create-form')
    var $myTable = $('.table')

    $myForm.submit(function (event) {
        event.preventDefault()
        var $formData = $(this).serialize()
        var $dataTarget = $myForm.attr('data-url')
        $('#submit-btn').attr('disabled', true)
        $.ajax({
            method: "POST",
            url: $dataTarget,
            data: $formData,
            beforeSend: function () {
                $("#loader").show()
            },
            success: function () {
                $myForm.trigger('reset')
                $myTable.load($dataTarget + ' .table')
            },
            complete: function () {
                $('#submit-btn').attr('disabled', false)
                $("#loader").hide()
            }
        })
    })
    var $sidebar = $('.col-sm-4')
    $('div').on('click', 'a.item', function (event) {
        event.preventDefault()
        var $targetUrl = $(this).attr('href')
        $.ajax({
            method: "GET",
            url: $targetUrl,
            beforeSend: function () {
                $("#loader").show()
            },
            success: function () {
                $sidebar.load($targetUrl + " div.details")
            },
            complete: function () {
                $("#loader").hide();
            },
        })
    })
    var $form2 = $("#search-form")
    $form2.submit(function (event) {
        event.preventDefault()
        $('#search-btn').attr('disabled', true)
        var $target = $form2.attr('data-url')
        var $data = $(this).serialize()
        var $finalUrl = $target + "?" + $data
        $.ajax({
            method: "GET",
            beforeSend: function () {
                $("#loader").show()
            },
            url: $finalUrl,
            success: function () {
                $myTable.load($finalUrl + ' .table')
            },
            complete: function () {
                $('#search-btn').attr('disabled', false)
                $("#loader").hide();
            },
        })
    });
    $('a.item').click(function () {
        var $targetUrl = $(this).attr('data-url')
        var $sidebar = $('.col-sm-4')
        $.ajax({
            method: "GET",
            url: $targetUrl,
            success: $sidebar.load($targetUrl + " div.details"),
        })
    });
})