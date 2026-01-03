from fastapi import FastAPI
from uuid import uuid4

app = FastAPI()

rooms = {}

@app.get("/")
def root():
    return {"message": "Backend is running"}

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
    return {"room_id": room_id}

@app.get("/rooms")
def list_rooms():
    return rooms

