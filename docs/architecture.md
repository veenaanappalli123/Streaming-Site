# System Architecture

## Overview

This project is a “Watch Together” web application that allows multiple users to watch the same YouTube video in real time. All users stay synchronized using real-time communication.

The system is designed using a **client–server architecture**, which means:
- The frontend runs in the user’s browser
- The backend runs on a server
- Both communicate using defined communication methods

The architecture is kept simple and clear to make it easy to understand and explain.

---

## Main Components

The system has three main components:

1. Frontend (User Interface)
2. Backend (Server Logic)
3. External APIs (YouTube)

Each component has a specific responsibility.

---

## Frontend Architecture

The frontend is built using:
- HTML for structure
- CSS for layout and design
- JavaScript for logic and interaction

The frontend runs entirely in the browser.

### Frontend Responsibilities
- Display buttons, inputs, and video player
- Allow users to create rooms
- Allow users to paste YouTube URLs
- Control video playback (play, pause, change video)
- Send user actions to the backend
- Receive updates from the backend
- Display chat messages

The frontend **does not decide synchronization by itself**.  
It follows instructions sent by the backend to stay in sync.

---

## Backend Architecture

The backend is built using **FastAPI** and runs on a local server.

### Backend Responsibilities
- Create watch rooms
- Generate unique room IDs
- Manage WebSocket connections
- Store room state in memory
- Broadcast updates to all users in the same room

Each room keeps track of:
- Current video ID
- Playback time
- Play or pause state
- Connected users

Room data is stored in memory because this project focuses on real-time behavior rather than long-term storage.

---

## Communication Flow

The communication happens in two steps:

### Step 1: Room Creation (REST API)
- Frontend sends a request to the backend
- Backend creates a room
- Backend returns a room ID

### Step 2: Real-Time Synchronization (WebSocket)
- Frontend connects to backend using WebSocket
- User actions are sent to the backend
- Backend broadcasts actions to all connected users
- All users stay synchronized

---

## External API Usage

The frontend uses the **YouTube IFrame API** to:
- Embed YouTube videos
- Control playback programmatically

The backend does not interact with YouTube directly.

---

## Why This Architecture Was Chosen

- Separates frontend and backend responsibilities
- WebSockets enable real-time synchronization
- REST API is simple and suitable for room creation
- Easy to debug and explain for an academic project
- Scalable to multiple users and rooms

This architecture balances simplicity and functionality.
