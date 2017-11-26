function convert() {
    
    obj_from = document.getElementById("converter-unit-from-value");
    value = Number(obj_from.value);

    if (value) {
        item = document.getElementById("calc_result")
        item.innerHTML = "Вам уже " +value*7+ " по собачьим меркам!";
    }
    else {
        item.innerHTML = "Пожалйста, введите число!";
    }
    
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