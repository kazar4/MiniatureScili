
let webSocket = new WebSocket("wss://kazar4.com:9001");
webSocket.addEventListener("open", (event) => {
    webSocket.send("player1");
});

function buttonClicked(buttonName) {

    if (buttonName === "U") {
        webSocket.send("U");
    } else if (buttonName === "R") {
        webSocket.send("R");
    } else if (buttonName === "D") {
        webSocket.send("D");
    } else if (buttonName === "L") {
        webSocket.send("L");
    } else if (buttonName === "DISCONNECT") {
        webSocket.send("DISCONNECT");
    } else if (buttonName === "PONG") {
        webSocket.send("PONG");
    } else if (buttonName === "RAINBOW") {
        webSocket.send("RAINBOW");
    } else if (buttonName === "SCORE") {
        webSocket.send("SCORE");
    }
}

