# Project Setup Guide

This document explains how to set up and run the project locally.

## Requirements

- Python 3.9 or higher
- pip
- A modern web browser


## Backend Setup
1. Navigate to the backend directory:
cd backend

2.Install dependencies:
pip install -r requirements.txt

3.Start the backend server:
python -m uvicorn main:app --reload

4.Verify the server is running:
http://127.0.0.1:8000
http://127.0.0.1:8000/docs

Frontend Setup
--------------
1)Open the frontend folder
2)Open index.html in a web browser
3)Enter a room ID to join a session
The backend must be running before opening the frontend
No database setup is required


