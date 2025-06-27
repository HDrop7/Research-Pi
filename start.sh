#!/bin/bash

# Startup script for Mac OS and Linux

echo "Starting up Research Pi"

open ./frontend/index.html &
FRONTEND_PID=$!

echo "Booting up virtual environment..."
source ./backend/venv/bin/activate

echo "Ctrl + C to stop the server"
cd ./backend
uvicorn main:app --reload

echo "Backend down. Close the frontend window, it no longer works."