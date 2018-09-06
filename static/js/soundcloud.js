/**
 * Created by ian on 5/15/18.
 */


let Soundcloud = {
    endpoint:"/api/soundcloud",
    resolve:function (url, callback) {
        $.ajax({
            url: Soundcloud.endpoint + "/resolve?url=" + encodeURI(url),
            method:"GET",
            complete:function (xhr, status) {
                if(callback)callback(xhr.responseJSON);
            }
        });
    },
};