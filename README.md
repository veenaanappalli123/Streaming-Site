# Watch Together – Real-Time Video Synchronization Web App

## Overview
This project is a **Watch Together web application** that allows multiple users to watch the same YouTube video in real time while staying synchronized. Users can create or join a room, select a video, control playback (play/pause), and chat with others in the same room.

The main learning objective of this project is to understand **real-time communication**, **client–server architecture**, and **WebSocket-based synchronization**.

---

## Features
- Create and join watch rooms using a unique Room ID
- Real-time video synchronization (play, pause, change video)
- Live chat between users in the same room
- Uses YouTube IFrame API for legal and reliable video playback
- Backend-controlled synchronization using WebSockets

---

## Project Structure

```text
Streaming-Site/
│
├── backend/
│   ├── main.py              # FastAPI backend with WebSocket logic
│   └── requirements.txt     # Backend dependencies
│
├── frontend/
│   ├── index.html           # Frontend UI
│   ├── style.css            # Styling
│   └── script.js            # Frontend logic and WebSocket handling
│
├── docs/
│   ├── architecture.md      # System architecture explanation
│   ├── api.md               # API documentation
│   ├── synchronization.md   # Video synchronization logic
│   ├── setup.md             # Setup and run instructions
│   └── contribution.md      # Development process and challenges
│
├── .gitignore
└── README.md








Technologies Used
Backend

Python
FastAPI – for REST API and WebSocket support
Uvicorn – ASGI server
WebSockets – for real-time communication

Frontend
HTML – structure
CSS – layout and design
JavaScript – application logic
YouTube IFrame API – embedded video playback and control

Why These Technologies Were Used
FastAPI: Lightweight, easy to use, and supports WebSockets natively.
WebSockets: Required for real-time synchronization and instant updates.
REST API: Used for simple, one-time operations like room creation.
YouTube IFrame API: Ensures legal video playback without handling video streams.
In-memory storage: Keeps the project simple and focused on real-time behavior.

How the Application Works (High-Level)
A user creates a room using a REST API call.
The backend generates a unique Room ID.
Users join the room using the same Room ID.
A WebSocket connection is established for each user.
When a user performs an action (play, pause, change video):
The action is sent to the backend.
The backend broadcasts it to all users in the room.
All users apply the same action locally, staying synchronized.



Limitations
Room data is stored in memory (lost on server restart)
No authentication system
Minor synchronization delays may occur due to network latency
Designed as a learning project, not a production system

Learning Outcomes
Understanding of client–server architecture
Real-time communication using WebSockets
Event-driven programming
API design and documentation
Integration of third-party APIs

