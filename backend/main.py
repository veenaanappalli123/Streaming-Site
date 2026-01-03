from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from uuid import uuid4

app = FastAPI()

rooms = {}
connections = {}

@app.post("/create-room")
def create_room():
    room_id = str(uuid4())
    rooms[room_id] = {
        "users": [],
        "video_state": {
            "playing": False,
            "time": 0
        }
    }
    connections[room_id] = []
    return {"room_id": room_id}

@app.websocket("/ws/{room_id}")
async def websocket_endpoint(websocket: WebSocket, room_id: str):
    await websocket.accept()

    if room_id not in connections:
        await websocket.close()
        return

    connections[room_id].append(websocket)

    try:
        while True:
            data = await websocket.receive_json()

            # Broadcast to all users in the room
            for conn in connections[room_id]:
                await conn.send_json(data)

    except WebSocketDisconnect:
        connections[room_id].remove(websocket)
