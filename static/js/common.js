


function Form2Object(form){
    let data = $(form).serializeArray();
    let obj = {};
    
    $.each(data, function (i, param) {
        obj[param.name] = param.value;
    });
    return obj;
}

function escapeHtml(unsafe) {
    return unsafe
         .replace(/&/g, "&amp;")
         .replace(/</g, "&lt;")
         .replace(/>/g, "&gt;")
         .replace(/"/g, "&quot;")
         .replace(/'/g, "&#039;");
 }


function FetchImages(callback){
    $.ajax({
        url:'/api/images',
        success:function(data){
            console.log(data);
            callback(data);
        }
    })
}

function LoadImage(container){
    if(container.classList.contains('loads-image')){
        let imageSrc = container.getAttribute('data-image');
        let img = document.createElement('img');
        img.onload = function () {
            container.style.backgroundImage = "url('" + imageSrc + "')";
            container.style.opacity = 1;
        };
        img.src = imageSrc;
    }
}