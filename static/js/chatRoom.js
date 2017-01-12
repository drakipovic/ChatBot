$(document).ready(function(){
    var socket = io.connect('http://' + document.domain + ':' + location.port);

    socket.on('response', function(msg) {
        var d = new Date();
        $('#chat_area').append(d.getHours() + ':' + d.getMinutes() + " bot" + ": " + msg.data + "\n");
    });

    var username = null;

    function save_username(username){
        username = username;
        $("#welcome").text("Welcome to chat bot " + username + ". It's great having you here! Ask any question you want.");
    }

    $("#message").keypress(function(event) {
        if (event.which == 13) {
            var msg = $('#message').val();
            socket.emit('question', {data: msg});
            var d = new Date();
            $('#message').val("");
            $('#chat_area').append(d.getHours() + ':' + d.getMinutes() + " me: " + msg + "\n");
        }      
    });

    $("#loginForm").submit(function(e) {
        $("#login").hide();
        $("#chat").show();
        var url = "/api/login"; // the script where you handle the form input.

        $.ajax({
            type: "POST",
            url: url,
            data: $("#loginForm").serialize(), // serializes the form's elements.
            success: function(data){
                save_username(data["username"]);
            }
        });

        e.preventDefault(); // avoid to execute the actual submit of the form.
    });
});