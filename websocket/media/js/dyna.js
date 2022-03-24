var connection = new WebSocket("ws://" + location.host + "/socket");
// var connection = new WebSocket("ws://" + location.host + "/wsocket");

// console.log(location.host)

connection.onopen = function() {
    console.log('connection opened');
    // connection.send('start');
};

connection.onmessage = function(evt) {
    document.getElementById('demo').innerHTML = evt.data;
};

connection.onclose = function() {
    console.log('connection closed');
};

function sendData(username)
{
    if(username == ""){
        username = 'Field is Require';
    }
    if(connection.readyState == 1) {
        connection.send(username);
    } else {
        alert('connection closed already');
    }
}
