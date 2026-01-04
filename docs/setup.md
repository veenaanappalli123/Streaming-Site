# Project Setup Guide

This document explains how to set up and run the project locally.

---

## System Requirements

- Python 3.10 or higher
- Git
- A modern web browser (Chrome, Edge, Firefox)

---

## Backend Setup

1. Open a terminal
2. Navigate to the backend folder

```bash
cd backend
Install required dependencies

bash
Copy code
pip install fastapi
pip install "uvicorn[standard]"
Start the backend server

bash
Copy code
python -m uvicorn main:app --host 127.0.0.1 --port 7777
Backend will run at:

cpp
Copy code
http://127.0.0.1:7777
Leave this terminal running.

Frontend Setup
Open a new terminal

Navigate to the frontend folder

bash
Copy code
cd frontend
Start the frontend server

bash
Copy code
python -m http.server 5500
Open a browser and visit:

cpp
Copy code
http://127.0.0.1:5500
How to Use the Application
Open the frontend in the browser

Click "Create Room"

Copy the generated Room ID

Share the Room ID with other users

Paste a YouTube video URL

Use play and pause controls to watch together

Use chat to communicate in real time

Stopping the Application
Press Ctrl + C in the backend terminal

Press Ctrl + C in the frontend terminal
