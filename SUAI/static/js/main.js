$(document).ready(function() {
    $('#auth-input-error').fadeOut(0);
});

function ajax_login() {

    var data = {
        'login': $('#auth-login')[0].value,
        'password': $('#auth-password')[0].value
    };

    console.log(data);

    $.ajax({

        data: data,
        dataType: "json",
        url: '/user/login/',

        success: function(result) {
            if (result['response'] == 'success') {
                $('.auth').html(result['html'])
            }
            else {
                auth_input_error_toogle();
            }
        }

    });
}

function ajax_logout() {

    $.ajax({

        url: '/user/logout/',
        success: function(result) {
            $('.auth').html(result['response']);
            $('#auth-input-error').fadeOut(0);
        }
    });

}

function auth_input_error_toogle() {
    console.log($('#auth-input-error')[0].style.display);
    if ($('#auth-input-error')[0].style.display) {
      $('#auth-input-error').fadeIn(500);
    } else {
      $('#auth-input-error').fadeOut(500);
    }
}

function convert() {
    
    obj_from = document.getElementById("converter-unit-from-value");
    value = Number(obj_from.value);
    
    meters_from_obj = document.getElementById("converter-unit-from");
    meters_from = Number(meters_from_obj.value);
    
    meters_to_obj = document.getElementById("converter-unit-to");
    meters_to = Number(meters_to_obj.value);
    
    obj_result = document.getElementById("converter-unit-to-value");
    obj_result.value = value*meters_from / meters_to;
    
}


function getName(str){
    if (str.lastIndexOf('\\')){
        var i = str.lastIndexOf('\\')+1;
    }
    else{
        var i = str.lastIndexOf('/')+1;
    }
    var filename = str.slice(i);
    var uploaded = document.getElementById("fileformlabel");
    uploaded.innerHTML = filename;
}

function news_addform_close() {

    button_add = document.getElementById("button_create");
    button_add.style.removeProperty('display');

    form_add = document.getElementsByClassName("news-add")[0];
    form_add.style.display = 'None';

}


function news_addform_show() {

    button_add = document.getElementById("button_create");
    button_add.style.display = 'None';

    form_add = document.getElementsByClassName("news-add")[0];
    form_add.style.removeProperty('display');

}