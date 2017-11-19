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