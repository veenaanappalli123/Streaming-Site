# Video Synchronization Logic

This document explains how video playback synchronization is implemented.

## Synchronization Model
The project uses an **event-based synchronization model**.
Instead of streaming video data, the system synchronizes:
- play events
- pause events
- seek events (timestamp changes)
Each client applies the same event locally.

## Workflow
1. A user joins a room
2. The frontend opens a WebSocket connection
3. The YouTube video is loaded locally
4. When a control action occurs:
   - the frontend sends an event to the backend
5. The backend broadcasts the event to all connected users
6. Each client applies the event to its video player

## Host Logic
Any connected user can trigger playback events.  
All users receive the same events in real time.

## Latency Considerations
- Network latency can cause small timing differences
- Exact synchronization is not guaranteed
- Minor desynchronization is acceptable for this use case

## Advantages of This Approach
- No video data is transmitted
- Scales easily with multiple users
- Avoids copyright and DRM issues
