# Backend API Documentation

This document describes the API exposed by the backend server.

---

## REST Endpoints

### Create Room

**Endpoint:** `POST /create-room`

Creates a new watch room.

**Response:**
```json
{
  "room_id": "string"
}

_______________________________________________________________________________________
WebSocket Endpoint
WebSocket Connection

Endpoint: /ws/{room_id}

Clients connect to this endpoint to:
1)synchronize video playback
2)send and receive chat messages
__________________________________________________________________________________________

WebSocket Message Format
All messages are sent as JSON objects.
_______________________________________
Video Control Messages:

Play video

{
  "type": "play",
  "time": 120
}

Pause video

{
  "type": "pause",
  "time": 135
}

Chat Message
{
  "type": "chat",
  "user": "username",
  "message": "Hello everyone"
}

______________________________________________________________________________________________

API Design Choices

JSON was chosen for readability and simplicity.
A single WebSocket connection handles both synchronization and chat.
The backend does not validate video IDs, as videos are managed client-side.



