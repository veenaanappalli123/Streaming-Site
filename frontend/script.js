
// Global variables
let socket = null;
let player = null;
let roomId = null;
function extractVideoId(url) {
    const match = url.match(
        /(?:youtube\.com\/watch\?v=|youtu\.be\/)([^&]+)/
    );
    return match ? match[1] : null;
}

let isHost = true; // first user is host by default ,well deserved hehe

// WebSocket connection
function connectWebSocket() {
    socket = new WebSocket(`ws://localhost:8000/ws/${roomId}`);

    socket.onopen = () => {
        console.log("Connected to WebSocket");
    };

    socket.onmessage = (event) => {
        const data = JSON.parse(event.data);

        if (data.type === "play") {
            player.seekTo(data.time, true);
            player.playVideo();
        }

        if (data.type === "pause") {
            player.seekTo(data.time, true);
            player.pauseVideo();
        }

        if (data.type === "chat") {
            displayChatMessage(data.user, data.message);
        }

        if (data.type === "video") {
            player.loadVideoById(data.videoId);
        }

    };

    socket.onclose = () => {
        console.log("WebSocket connection closed");
    };
}

// YouTube Player Setup
function onYouTubeIframeAPIReady() {
    player = new YT.Player("player", {
        height: "360",
        width: "640",
        videoId: "dQw4w9WgXcQ", // default video
        events: {
            onReady: onPlayerReady
        }
    });
}

function onPlayerReady() {
    console.log("YouTube Player Ready");
}

// Video control handlers
function playVideo() {
    const time = player.getCurrentTime();
    player.playVideo();

    socket.send(JSON.stringify({
        type: "play",
        time: time
    }));
}

function pauseVideo() {
    const time = player.getCurrentTime();
    player.pauseVideo();

    socket.send(JSON.stringify({
        type: "pause",
        time: time
    }));
}  

function loadVideo() {
    const input = document.getElementById("video-url");
    const videoId = extractVideoId(input.value);

    if (!videoId) {
        alert("Invalid YouTube URL");
        return;
    }

    socket.send(JSON.stringify({
        type: "video",
        videoId: videoId
    }));
}



// Chat logic
function sendChatMessage() {
    const input = document.getElementById("chat-input");
    const message = input.value;

    if (message.trim() === "") return;

    socket.send(JSON.stringify({
        type: "chat",
        user: "User",
        message: message
    }));

    input.value = "";
}

function displayChatMessage(user, message) {
    const chatBox = document.getElementById("chat-box");
    const msg = document.createElement("div");
    msg.textContent = `${user}: ${message}`;
    chatBox.appendChild(msg);
}


// Room initialization
async function createRoom() {
    const response = await fetch("http://localhost:8000/create-room", {
        method: "POST"
    });

    const data = await response.json();
    roomId = data.room_id;

    document.getElementById("room-id").textContent = roomId;

    connectWebSocket();
}


// Button bindings
document.getElementById("create-room-btn").onclick = createRoom;
document.getElementById("play-btn").onclick = playVideo;
document.getElementById("pause-btn").onclick = pauseVideo;
document.getElementById("send-btn").onclick = sendChatMessage;
document.getElementById("load-video-btn").onclick = loadVideo;
