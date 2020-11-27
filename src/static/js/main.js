

$(document).ready(function () {
    // Listen to click event on the submit button

    var input = $('.validate-input .input100');


    $('#button').click(function (e) {

        e.preventDefault();

        for(var i=0; i<input.length; i++) {
            if(validate(input[i]) == false ){
                showValidate(input[i]);

                return false;
            }

            if(validateUser() == false){
                
              alert('User not found.')
                return false;
            }

            window.location.href = "shareholder";
        }



    });

    function showValidate(input) {
        var thisAlert = $(input).parent();

        $(thisAlert).addClass('alert-validate');
    }

    function hideValidate(input) {
        var thisAlert = $(input).parent();

        $(thisAlert).removeClass('alert-validate');
    }

    function validateUser(){

        if($('#username').val().trim() != 'ahmed.oladapo@africaprudential.com' && $('#password').val().trim() != 'admin'){
            return false;
        }
    }

    function validate (input) {
        if($(input).attr('type') == 'email' || $(input).attr('name') == 'email') {
            if($(input).val().trim().match(/^([a-zA-Z0-9_\-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([a-zA-Z0-9\-]+\.)+))([a-zA-Z]{1,5}|[0-9]{1,3})(\]?)$/) == null) {
                return false;
            }
        }
        else {
            if($(input).val().trim() == ''){
                return false;
            }
        }
    }

});
