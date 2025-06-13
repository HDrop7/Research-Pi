#!/bin/bash

# Startup script for Mac OS and Linux

echo "Starting up Research Pi"

open ./frontend/index.html &

echo "Booting up virtual environment..."
source ./backend/venv/bin/activate

cd ./backend
uvicorn main:app --reload

echo "Running. Crtl + C to stop the server"
