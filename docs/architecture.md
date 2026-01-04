# System Architecture

This project follows a **client–server architecture** designed for real-time collaboration.

The system is divided into three main components:
- Frontend (client-side)
- Backend (server-side)
- External video provider (YouTube)

## High-Level Architecture
Each user accesses the website through a web browser. The frontend embeds a YouTube video and connects to the backend using WebSockets.

The backend manages rooms and synchronizes events between connected users. Video streaming itself is handled entirely by YouTube.

## Components Description ##
### Frontend
The frontend is responsible for:
- Displaying the user interface
- Embedding the YouTube video using the YouTube IFrame API
- Sending playback and chat events to the backend
- Receiving synchronization events from the backend

Technologies used:
- HTML
- CSS
- JavaScript

### Backend
The backend acts as the synchronization server. It:
- Creates and manages rooms
- Tracks connected users
- Broadcasts synchronization events
- Handles real-time chat messages

Technologies used:
- Python
- FastAPI
- WebSockets

The backend does **not** stream or store video content.

### YouTube
YouTube provides the video stream using the official YouTube IFrame API.  
Each client loads the video independently, ensuring legality and scalability.

## Architectural Decisions
- **WebSockets** were chosen for real-time, bidirectional communication.
- **FastAPI** was selected for its simplicity and WebSocket support.
- Video streaming was delegated to YouTube to avoid legal and technical complexity.

## Limitations

- The backend stores room data in memory (no persistence).
- Perfect synchronization cannot be guaranteed due to network latency.
