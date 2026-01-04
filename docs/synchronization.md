
# Synchronization Strategy

## Overview

The core feature of this project is real-time synchronization. All users in the same room must watch the same video at the same playback position.

This synchronization is achieved using WebSockets and a server-controlled approach.

---

## Synchronization Approach Used

This project uses a **server-authoritative synchronization model**.

This means:
- The server controls the shared state
- Clients do not synchronize directly with each other
- All updates pass through the backend

---

## How Synchronization Works

1. A user performs an action (play, pause, change video)
2. The frontend sends this action to the backend using WebSocket
3. The backend receives the event
4. The backend broadcasts the event to all connected users
5. All users update their video state accordingly

This ensures all users remain synchronized.

---

## Events That Are Synchronized

The following events are synchronized in real time:
- Play video
- Pause video
- Change video
- Chat messages

Each event includes necessary data such as:
- Playback timestamp
- Video ID
- Message content

---

## Why Server-Authoritative Model?

This model was chosen because:
- It prevents users from going out of sync
- There is a single source of truth
- It avoids conflicts between users
- It is easier to debug and maintain

This approach is commonly used in real-time collaborative systems.

---

## Handling Multiple Users

Multiple users can connect to the same room using the room ID.

- Each user opens a WebSocket connection
- All connections are stored on the backend
- Broadcast messages reach all connected users

---

## Handling Late Joiners

When a new user joins:
- The WebSocket connection is established
- The user immediately starts receiving synchronization updates
- The user synchronizes with the current room state

---

## Limitations

- Room state is stored in memory
- Server restart clears all active rooms

These limitations are acceptable for an academic demonstration project.
