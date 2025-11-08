"""
Launcher script for Converso Downloader
Properly launches the Streamlit application in production mode
"""

import sys
import os
from pathlib import Path
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
    
    # Set Streamlit config directory to use bundled config
    config_dir = os.path.join(application_path, '.streamlit')
    if os.path.exists(config_dir):
        os.environ['STREAMLIT_CONFIG_DIR'] = config_dir
    
    # Set production mode configuration via environment variables
    os.environ['STREAMLIT_BROWSER_GATHER_USAGE_STATS'] = 'false'
    os.environ['STREAMLIT_SERVER_HEADLESS'] = 'true'
    os.environ['STREAMLIT_GLOBAL_DEVELOPMENT_MODE'] = 'false'
    
    # Launch streamlit with the app in production mode
    sys.argv = [
        "streamlit",
        "run",
        app_path,
        "--server.headless=true",
        "--browser.gatherUsageStats=false",
        "--global.developmentMode=false",
        "--server.enableXsrfProtection=false",
        "--server.enableCORS=false"
    ]
    
    sys.exit(stcli.main())
