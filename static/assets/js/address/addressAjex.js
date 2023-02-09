function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


jQuery(function($){
    $(document).ready(function(){
        $("#id_country").change(function(){
            $.ajax({
                url:"/state/",
                type:"POST",
                data:{country: $(this).val(),},
                success: function(result) {
                    console.log(result);
                    cols = document.getElementById("id_state");
                    cols.options.length = 0;
                    cols.options.add(new Option("State", "State"));
                    for(var k in result){
                        cols.options.add(new Option(k, result[k]));
                    }
                },
                headers: {
                    "X-CSRFToken": {{csrf_token}}
                },
                error: function(e){
                    console.error(JSON.stringify(e));
                },
            });
        });
        $("#id_state").change(function(){
            $.ajax({
                url:"/city/",
                type:"POST",
                data:{state: $(this).val(),},
                success: function(result) {
                    console.log(result);
                    cols = document.getElementById("id_city");
                    cols.options.length = 0;
                    cols.options.add(new Option("City", "City"));

                    for(var k in result){
                        cols.options.add(new Option(k, result[k]));
                    }
                },
                headers: {
                    "X-CSRFToken": {{csrf_token}}
                },
                error: function(e){
                    console.error(JSON.stringify(e));
                },
            });
        });
    }); 
});