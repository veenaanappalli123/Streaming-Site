Frontend – Watch Together Website
_________________________________

This folder contains the **frontend implementation** of the Watch Together website.
The frontend is responsible for the user interface, video playback, user interactions,
and communication with the backend server

................
Files Overview
................

frontend/
├── index.html # Main HTML structure
├── style.css # Styling and layout
├── script.js # Frontend logic (WebSocket, sync, chat)
└── README.md # Frontend documentation

The frontend handles:
- Displaying the user interface
- Embedding the YouTube video player
- Sending play/pause events to the backend
- Receiving synchronization events
- Displaying real-time chat messages

The frontend does not stream video data.  
All video content is loaded directly from YouTube.


HTML Structure --- index.html
--------------
The HTML file defines:
- A video section containing the YouTube player
- Control buttons (create room, play, pause)
- A chat section for real-time messaging
- Required elements with specific IDs used by JavaScript

Important IDs used by the script:
- `player` – YouTube video container
- `create-room-btn` – creates a new room
- `play-btn` / `pause-btn` – video controls
- `chat-box` – displays chat messages
- `chat-input` – user message input
- `send-btn` – sends chat message

Styling --- style.css
-------
The CSS file:
- Uses Flexbox for layout
- Separates video and chat sections visually
- Keeps styling simple and readable
- Avoids external frameworks for clarity

The design focuses on:
- usability
- clean layout
- easy readability

Frontend Logic --- script.js
----------------------------
The JavaScript file implements:
- WebSocket connection to the backend
- YouTube IFrame API integration
- Video synchronization logic
- Real-time chat handling

### WebSocket Communication
- Connects to `/ws/{room_id}`
- Sends JSON messages for play, pause, and chat
- Receives synchronization events from the backend

### Video Synchronization
- Captures the current playback timestamp
- Sends timestamped events to the backend
- Applies received events locally to stay in sync

### Chat
- Messages are sent as structured JSON
- Incoming messages are displayed immediately
- Uses the same WebSocket connection as synchronization


---------------------▶️ How to Run the Frontend----------------------

1. Make sure the backend server is running
2. Open `index.html` in a web browser
3. Click **Create Room**
4. Share the Room ID with other users
5. Start watching and chatting together







[⚠️ Notes & Limitations
- The frontend assumes the backend runs on `localhost:8000`
- Video synchronization may have minor delays due to network latency
- No user authentication is implemented]


The frontend provides a simple but functional interface that demonstrates:
- real-time communication
- client-side event handling
- interaction with a backend synchronization server

It is designed to be easy to understand, maintain, and extend


