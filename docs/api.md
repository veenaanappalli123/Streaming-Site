# API Documentation

## What is an API?

API stands for Application Programming Interface.

An API allows different parts of a software system to communicate with each other in a structured and controlled way. Instead of accessing internal code directly, one part sends a request and receives a response.

In this project, APIs are used to connect:
- Frontend and backend
- Backend and multiple users
- Frontend and YouTube services

---

## APIs Used in This Project

This project uses three main APIs:
1. REST API (Backend)
2. WebSocket API (Backend)
3. YouTube IFrame API (External)

Each API has a specific role.

---

## REST API (Backend)

### POST /create-room

This API endpoint is used to create a new watch room.

### Purpose
- Generate a unique room ID
- Initialize room state on the backend

### Request
```http
POST /create-room
Response
json
Copy code
{
  "room_id": "unique-room-id"
}
Why REST API is Used Here
Room creation is a simple one-time operation

REST APIs are easy to implement and understand

Suitable for request–response communication

WebSocket API (Backend)
Endpoint
perl
Copy code
ws://<server>/ws/{room_id}
Purpose
WebSocket API is used for real-time communication between users in the same room.

What It Handles
Play video events

Pause video events

Video change events

Chat messages

Why WebSocket Is Used
Keeps a persistent connection open

Low latency communication

Allows instant synchronization

Ideal for real-time collaborative applications

When one user performs an action, the backend broadcasts it to all users connected to the same room.

YouTube IFrame API
The frontend uses the YouTube IFrame API to control video playback.

What It Is Used For
Embedding YouTube videos

Playing and pausing videos

Seeking to specific timestamps

Loading videos dynamically

Why This API Is Required
YouTube restricts direct video control

Official API ensures proper usage

Provides reliable playback control

The backend does not directly interact with YouTube; all video control is handled on the frontend.
