@echo off
echo.
echo ========================================
echo   Converso Downloader v2.1.3
echo   Professional YouTube Downloader
echo.
echo   Created by Converso Empire
echo   https://github.com/Converso-Empire
echo ========================================
echo.
echo Starting application...
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8 or higher from python.org
    pause
    exit /b 1
)

REM Check if requirements are installed
python -c "import streamlit" >nul 2>&1
if errorlevel 1 (
    echo Installing requirements...
    pip install -r requirements.txt
    if errorlevel 1 (
        echo ERROR: Failed to install requirements
        pause
        exit /b 1
    )
)

REM Check if FFmpeg is available
ffmpeg -version >nul 2>&1
if errorlevel 1 (
    echo.
    echo WARNING: FFmpeg is not installed or not in PATH
    echo FFmpeg is required for audio extraction and video merging
    echo Please install FFmpeg from: https://ffmpeg.org/download.html
    echo.
    echo The app will start, but some features may not work.
    echo.
    timeout /t 5
)

REM Start the application
echo.
echo Opening Converso Downloader...
echo.
echo The app will open in your default browser.
echo To stop the app, close this window or press Ctrl+C
echo.

streamlit run app.py

pause
