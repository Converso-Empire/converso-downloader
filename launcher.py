"""
Launcher script for Converso Downloader
Properly launches the Streamlit application
"""

import sys
import os
from streamlit.web import cli as stcli

if __name__ == '__main__':
    # Get the directory where the executable is located
    if getattr(sys, 'frozen', False):
        # Running as compiled executable
        application_path = sys._MEIPASS
    else:
        # Running as script
        application_path = os.path.dirname(os.path.abspath(__file__))
    
    # Path to the main app
    app_path = os.path.join(application_path, 'app.py')
    
    # Launch streamlit with the app
    sys.argv = [
        "streamlit",
        "run",
        app_path,
        "--server.headless=true",
        "--browser.gatherUsageStats=false",
        "--server.port=8501",
        "--server.address=localhost"
    ]
    
    sys.exit(stcli.main())
