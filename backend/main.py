from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from typing import Dict, List
import json

app = FastAPI()

# Allow frontend to talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for college project
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------
# In-memory room storage
# -----------------------------
# Example structure:
# rooms = {
#   "room1": {
#       "video_id": "abc123",
#       "timestamp": 12.5,
#       "is_playing": True,
#       "connections": [WebSocket, WebSocket]
#   }
# }

rooms: Dict[str, Dict] = {}


# -----------------------------
# Basic test endpoint
# -----------------------------
@app.get("/")
def root():
    return {"message": "Backend running successfully"}


# -----------------------------
# WebSocket for room sync + chat
# -----------------------------
@app.websocket("/ws/{room_id}")
async def websocket_endpoint(websocket: WebSocket, room_id: str):
    await websocket.accept()

    # Create room if not exists
    if room_id not in rooms:
        rooms[room_id] = {
            "video_id": None,
            "timestamp": 0,
            "is_playing": False,
            "connections": []
        }

    rooms[room_id]["connections"].append(websocket)

    try:
        while True:
            data = await websocket.receive_text()
            message = json.loads(data)

            event_type = message.get("type")

            # -----------------------------
            # Video control events
            # -----------------------------
            if event_type == "video_state":
                rooms[room_id]["video_id"] = message["video_id"]
                rooms[room_id]["timestamp"] = message["timestamp"]
                rooms[room_id]["is_playing"] = message["is_playing"]

                await broadcast(room_id, message)  
            elif event_type == "video":
                rooms[room_id]["video_id"] = message["videoId"]
                rooms[room_id]["timestamp"] = 0
                rooms[room_id]["is_playing"] = False

                await broadcast(room_id, message)
            # -----------------------------
            # Chat messages
            # -----------------------------
            elif event_type == "chat":
                await broadcast(room_id, message)

    except WebSocketDisconnect:
        rooms[room_id]["connections"].remove(websocket)

        if len(rooms[room_id]["connections"]) == 0:
            del rooms[room_id]


# -----------------------------
# Broadcast helper
# -----------------------------
async def broadcast(room_id: str, message: dict):
    dead_connections = []

    for connection in rooms[room_id]["connections"]:
        try:
            await connection.send_text(json.dumps(message))
        except:
            dead_connections.append(connection)

    for dc in dead_connections:
        rooms[room_id]["connections"].remove(dc)
