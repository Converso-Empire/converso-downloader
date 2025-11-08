"""
Converso Downloader - Main Application
Professional YouTube downloader with smart search
Version: 2.1.4

Created by Converso Empire
https://github.com/Converso-Empire
© 2025 Converso Empire. All rights reserved.
"""

import streamlit as st
import os
from pathlib import Path

# Import version information
from version import __version__, __app_name__, __description__

# Import utilities
from utils.downloader import VideoInfoExtractor, VideoDownloader, PlaylistExtractor
from utils.format_handler import FormatProcessor
from utils.file_utils import FileManager
from utils.update_checker import UpdateChecker
from config.settings import SettingsManager

# Import UI components
from ui_components import (
    inject_custom_css,
    render_header,
    render_url_input,
    render_video_info_card,
    render_quick_download,
    render_custom_formats,
    render_advanced_settings,
    render_batch_download,
    render_footer
)

# Page Configuration
st.set_page_config(
    page_title=f"{__app_name__} v{__version__} - {__description__}",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="collapsed"
)


def init_session_state():
    """Initialize all session state variables"""
    defaults = {
        'initialized': True,
        'current_url': '',
        'video_info': None,
        'selected_quality': 'best',
        'download_queue': [],
        'recent_urls': [],
        'batch_urls': [],
        'update_checked': False,
        'update_available': False,
        'update_info': None,
    }
    
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def check_for_updates():
    """Check for application updates"""
    if not st.session_state.update_checked:
        try:
            from version import __version__, __repo__
            checker = UpdateChecker(__version__, __repo__)
            update_available, release_info = checker.check_for_updates()
            
            st.session_state.update_checked = True
            st.session_state.update_available = update_available
            st.session_state.update_info = release_info
            
        except Exception as e:
            # Silently fail if update check doesn't work
            st.session_state.update_checked = True
            pass


def main():
    """Main application entry point"""
    # Inject custom CSS
    inject_custom_css()
    
    # Initialize session state
    if 'initialized' not in st.session_state:
        init_session_state()
    
    # Check for updates (only once per session)
    check_for_updates()
    
    # Display update notification if available
    if st.session_state.update_available and st.session_state.update_info:
        from version import __version__
        checker = UpdateChecker(__version__, "https://github.com/Converso-Empire/converso-downloader")
        update_message = checker.format_update_message(st.session_state.update_info)
        st.info(update_message, icon="🎉")
    
    # Initialize settings manager
    settings = SettingsManager()
    
    # Ensure download directory exists
    download_path = settings.get('download_location')
    FileManager.ensure_directory(download_path)
    
    # Header
    render_header()
    
    # Main Content
    with st.container():
        # URL Input
        url = render_url_input()
        
        if url:
            # Validate URL
            extractor = VideoInfoExtractor()
            is_valid, error_msg = extractor.validate_url(url)
            
            if not is_valid:
                st.error(f"❌ {error_msg}")
                return
            
            # Extract video info
            with st.spinner("🔍 Fetching video information..."):
                video_info = extractor.extract_info(url)
            
            if not video_info:
                st.error("❌ Failed to fetch video information. Please check the URL and try again.")
                return
            
            # Store in session state
            st.session_state.video_info = video_info
            
            # Video Information Card
            render_video_info_card(video_info)
            
            st.divider()
            
            # Download Options Tabs
            tab1, tab2, tab3, tab4 = st.tabs([
                "⚡ Quick Download",
                "🎯 Custom Formats",
                "⚙️ Advanced Settings",
                "📋 Batch Download"
            ])
            
            with tab1:
                render_quick_download(video_info, settings)
            
            with tab2:
                render_custom_formats(video_info, settings)
            
            with tab3:
                render_advanced_settings(settings)
            
            with tab4:
                render_batch_download()
    
    # Footer
    render_footer()


if __name__ == "__main__":
    main()
