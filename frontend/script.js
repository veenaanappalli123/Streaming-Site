const socket = new WebSocket("ws://localhost:8000");

socket.onopen = function () {
    console.log("Connected to WebSocket server");
};

socket.onmessage = function (event) {
    const chatBox = document.querySelector(".chat-messages");
    const message = document.createElement("p");
    message.textContent = event.data;
    chatBox.appendChild(message);
    chatBox.scrollTop = chatBox.scrollHeight;
};

document.querySelector(".play-btn").addEventListener("click", function () {
    socket.send("PLAY");
});

document.querySelector(".pause-btn").addEventListener("click", function () {
    socket.send("PAUSE");
});

document.querySelector(".send-btn").addEventListener("click", function () {
    const input = document.querySelector(".chat-input");
    const text = input.value;
    if (text !== "") {
        socket.send("CHAT: " + text);
        input.value = "";
    }
});