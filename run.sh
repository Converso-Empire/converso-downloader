#!/bin/bash

echo ""
echo "========================================"
echo "  Converso Downloader v2.1.3"
echo "  Professional YouTube Downloader"
echo ""
echo "  Created by Converso Empire"
echo "  https://github.com/Converso-Empire"
echo "========================================"
echo ""
echo "Starting application..."
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    if ! command -v python &> /dev/null; then
        echo "ERROR: Python is not installed"
        echo "Please install Python 3.8 or higher"
        exit 1
    else
        PYTHON_CMD="python"
    fi
else
    PYTHON_CMD="python3"
fi

echo "Using: $PYTHON_CMD"

# Check if pip is installed
if ! command -v pip3 &> /dev/null; then
    if ! command -v pip &> /dev/null; then
        echo "ERROR: pip is not installed"
        exit 1
    else
        PIP_CMD="pip"
    fi
else
    PIP_CMD="pip3"
fi

# Check if requirements are installed
$PYTHON_CMD -c "import streamlit" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "Installing requirements..."
    $PIP_CMD install -r requirements.txt
    if [ $? -ne 0 ]; then
        echo "ERROR: Failed to install requirements"
        exit 1
    fi
fi

# Check if FFmpeg is available
if ! command -v ffmpeg &> /dev/null; then
    echo ""
    echo "WARNING: FFmpeg is not installed"
    echo "FFmpeg is required for audio extraction and video merging"
    echo ""
    echo "To install FFmpeg:"
    echo "  macOS:   brew install ffmpeg"
    echo "  Linux:   sudo apt install ffmpeg"
    echo ""
    echo "The app will start, but some features may not work."
    echo ""
    sleep 3
fi

# Start the application
echo ""
echo "Opening Converso Downloader..."
echo ""
echo "The app will open in your default browser."
echo "To stop the app, press Ctrl+C in this terminal"
echo ""

streamlit run app.py
