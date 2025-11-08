"""
UI Components for Converso Downloader v2.1.3

Created by Converso Empire
https://github.com/Converso-Empire
© 2025 Converso Empire. All rights reserved.
"""

import streamlit as st
from typing import Dict, List
from pathlib import Path
import time

# Import version information
try:
    from version import __version__, __app_name__, __copyright__
except ImportError:
    __version__ = "2.1.3"
    __app_name__ = "Converso Downloader"
    __copyright__ = "© 2025 Converso Empire. All rights reserved."

from utils.format_handler import FormatProcessor
from utils.file_utils import FileManager
from utils.downloader import VideoDownloader, PlaylistExtractor
from utils.youtube_search import YouTubeSearcher
from config.settings import SettingsManager


def inject_custom_css():
    """Inject custom CSS for modern dark theme"""
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');
        
        * {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
        }
        
        .stApp {
            background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
            color: #f8fafc;
        }
        
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        
        .custom-card {
            background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
            border: 1px solid #334155;
            border-radius: 12px;
            padding: 1.5rem;
            margin: 1rem 0;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
            transition: all 0.3s ease;
        }
        
        .custom-card:hover {
            border-color: #2563eb;
            box-shadow: 0 8px 16px rgba(37, 99, 235, 0.2);
        }
        
        h1, h2, h3, h4, h5, h6 {
            color: #f8fafc !important;
            font-weight: 700;
        }
        
        .stTextInput input {
            background-color: #1e293b;
            border: 2px solid #334155;
            border-radius: 10px;
            color: #f8fafc;
            padding: 0.75rem 1rem;
            font-size: 1rem;
            transition: all 0.3s ease;
        }
        
        .stTextInput input:focus {
            border-color: #2563eb;
            box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.1);
        }
        
        .stButton button {
            background: linear-gradient(135deg, #2563eb 0%, #1e40af 100%);
            color: white;
            border: none;
            border-radius: 10px;
            padding: 0.625rem 1.5rem;
            font-weight: 600;
            font-size: 0.95rem;
            transition: all 0.3s ease;
            box-shadow: 0 4px 6px rgba(37, 99, 235, 0.3);
        }
        
        .stButton button:hover {
            background: linear-gradient(135deg, #1e40af 0%, #1e3a8a 100%);
            transform: translateY(-2px);
            box-shadow: 0 6px 12px rgba(37, 99, 235, 0.4);
        }
        
        .stProgress > div > div {
            background-color: #334155;
            border-radius: 10px;
            height: 12px;
        }
        
        .stProgress > div > div > div {
            background: linear-gradient(90deg, #2563eb 0%, #0ea5e9 100%);
            border-radius: 10px;
        }
        
        .stTabs [data-baseweb="tab-list"] {
            gap: 8px;
            background-color: transparent;
        }
        
        .stTabs [data-baseweb="tab"] {
            background-color: #1e293b;
            border-radius: 10px;
            color: #94a3b8;
            padding: 0.75rem 1.5rem;
            font-weight: 600;
            border: 2px solid transparent;
        }
        
        .stTabs [data-baseweb="tab"]:hover {
            background-color: rgba(37, 99, 235, 0.1);
            color: #3b82f6;
        }
        
        .stTabs [aria-selected="true"] {
            background: linear-gradient(135deg, #2563eb 0%, #1e40af 100%);
            color: white !important;
            border-color: #2563eb;
        }
        
        .quality-badge {
            background: linear-gradient(135deg, #2563eb 0%, #1e40af 100%);
            color: white;
            padding: 0.25rem 0.75rem;
            border-radius: 20px;
            font-size: 0.75rem;
            font-weight: 700;
            text-transform: uppercase;
            display: inline-block;
            margin: 0 0.25rem;
        }
        
        .codec-badge {
            background-color: rgba(148, 163, 184, 0.1);
            color: #94a3b8;
            padding: 0.25rem 0.625rem;
            border-radius: 6px;
            font-size: 0.75rem;
            font-weight: 600;
            font-family: 'Monaco', 'Courier New', monospace;
            display: inline-block;
            margin: 0 0.25rem;
        }
        
        .size-badge {
            background-color: rgba(16, 185, 129, 0.1);
            color: #10b981;
            padding: 0.25rem 0.625rem;
            border-radius: 6px;
            font-size: 0.75rem;
            font-weight: 600;
            display: inline-block;
            margin: 0 0.25rem;
        }
        
        .status-indicator {
            width: 8px;
            height: 8px;
            border-radius: 50%;
            display: inline-block;
            margin-right: 0.5rem;
        }
        
        .status-online {
            background-color: #10b981;
            box-shadow: 0 0 8px rgba(16, 185, 129, 0.5);
        }
        
        hr {
            margin: 2rem 0;
            border: none;
            height: 1px;
            background: linear-gradient(90deg, transparent 0%, #334155 50%, transparent 100%);
        }
    </style>
    """, unsafe_allow_html=True)


def render_header():
    """Render application header"""
    col1, col2, col3 = st.columns([2, 6, 2])
    
    with col1:
        st.markdown("""
            <div style="display: flex; align-items: center; gap: 0.75rem;">
                <span style="font-size: 2rem;">🎬</span>
                <span style="font-size: 1.5rem; font-weight: 700; color: #f8fafc;">
                    Converso <span style="color: #3b82f6;">Downloader</span>
                </span>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
            <div style="text-align: center; padding: 0.5rem;">
                <span style="color: #94a3b8; font-size: 0.875rem;">
                    v{__version__} • YouTube Downloader • Search & Download • Auto-Merge Highest Quality
                </span>
            </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
            <div style="text-align: right; padding: 0.5rem;">
                <span class="status-indicator status-online"></span>
                <span style="color: #10b981; font-size: 0.875rem; font-weight: 600;">Online</span>
            </div>
        """, unsafe_allow_html=True)


def render_url_input() -> str:
    """Render URL/Search input section with real-time YouTube search"""
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 6, 1])
    
    with col2:
        # Check if a video is already selected
        video_selected = st.session_state.get('selected_video_url') and st.session_state.get('current_input', '').startswith('http')
        
        if not video_selected:
            # Show search interface
            st.markdown("""
                <div style="text-align: center; margin-bottom: 1.5rem;">
                    <h2 style="font-size: 1.75rem; margin-bottom: 0.5rem;">
                        Search or Enter YouTube URL
                    </h2>
                    <p style="color: #94a3b8; font-size: 0.95rem;">
                        🔍 Search by name • Paste URL • Enter Video ID
                    </p>
                </div>
            """, unsafe_allow_html=True)
            
            # Main input field
            user_input = st.text_input(
                "Search or URL",
                value=st.session_state.get('current_input', ''),
                placeholder="Search: 'Best music 2024' or paste: 'https://youtube.com/watch?v=...' or ID: 'dQw4w9WgXcQ'",
                label_visibility='collapsed',
                key="search_input",
                help="Enter anything: video name, URL, or video ID"
            )
        else:
            # Video selected - hide search field and show only "New Search" button
            user_input = st.session_state.get('current_input', '')
            
            col_msg, col_btn = st.columns([4, 1])
            with col_msg:
                st.success("✅ Video selected! Scroll down to see details and download options.")
            with col_btn:
                if st.button("🔍 New Search", width='stretch', key="new_search_top"):
                    # Clear selection to start new search
                    st.session_state.selected_video_url = None
                    st.session_state.current_input = ''
                    st.session_state.hide_search = False
                    st.rerun()
            
            # Skip rest of the function - no search UI needed
            return st.session_state.get('selected_video_url', '')
        
        # Initialize searcher
        if 'youtube_searcher' not in st.session_state:
            st.session_state.youtube_searcher = YouTubeSearcher()
        
        searcher = st.session_state.youtube_searcher
        
        # Check if we should show search results or hide them
        show_search_results = True
        
        # If a video was just selected, hide search results and show confirmation
        if (st.session_state.get('selected_video_url') and user_input.startswith('http')) or st.session_state.get('hide_search', False):
            show_search_results = False
            
            # Show success message with new search button
            col_msg, col_btn = st.columns([4, 1])
            with col_msg:
                st.success("✅ Video selected! Scroll down to see details and download options.")
            with col_btn:
                if st.button("🔍 New Search", width='stretch'):
                    # Clear selection to start new search
                    st.session_state.selected_video_url = None
                    st.session_state.current_input = ''
                    st.session_state.hide_search = False
                    st.rerun()
        
        # Real-time search results
        if user_input and user_input.strip() and show_search_results:
            parsed = searcher.parse_input(user_input)
            
            # Show input type indicator
            if parsed['type'] == 'url':
                st.success("✅ YouTube URL detected")
                selected_url = user_input
                
            elif parsed['type'] == 'video_id':
                st.success(f"✅ Video ID detected: {parsed['value']}")
                selected_url = parsed['url']
                
            elif parsed['type'] == 'search_query':
                st.info(f"🔍 Searching YouTube for: '{parsed['value']}'")
                
                # Perform search with progress
                with st.spinner("Searching..."):
                    search_results = searcher.search(parsed['value'], max_results=8)
                
                if search_results:
                    st.markdown("### 📺 Search Results")
                    st.markdown(f"<p style='color: #94a3b8; font-size: 0.85rem; margin-bottom: 1rem;'>Found {len(search_results)} videos - Click ✓ Select to choose</p>", unsafe_allow_html=True)
                    
                    # Display search results with enhanced styling
                    for idx, video in enumerate(search_results):
                        # Each result in a clean container
                        col_thumb, col_info, col_btn = st.columns([1, 4, 1])
                        
                        with col_thumb:
                            thumbnail_url = video.get('thumbnail', '')
                            if thumbnail_url and thumbnail_url.strip():
                                try:
                                    st.image(thumbnail_url, width='stretch')
                                except Exception:
                                    # Fallback placeholder
                                    st.markdown("""
                                        <div style="width: 100%; aspect-ratio: 16/9; background: #1e293b; 
                                        display: flex; align-items: center; justify-content: center; 
                                        border-radius: 6px; border: 1px solid #334155;">
                                            <span style="font-size: 2rem;">🎬</span>
                                        </div>
                                    """, unsafe_allow_html=True)
                            else:
                                # No thumbnail available
                                st.markdown("""
                                    <div style="width: 100%; aspect-ratio: 16/9; background: #1e293b; 
                                    display: flex; align-items: center; justify-content: center; 
                                    border-radius: 6px; border: 1px solid #334155;">
                                        <span style="font-size: 2rem;">🎬</span>
                                    </div>
                                """, unsafe_allow_html=True)
                        
                        with col_info:
                            st.markdown(f"**{video['title']}**")
                            duration = int(video.get('duration', 0)) if video.get('duration') else 0
                            duration_str = f"{duration // 60}:{duration % 60:02d}" if duration else 'N/A'
                            st.markdown(f"<small style='color: #94a3b8;'>{video.get('uploader', 'Unknown')} • {duration_str} • {video.get('view_count', 0):,} views</small>", unsafe_allow_html=True)
                        
                        with col_btn:
                            # Use unique key with video ID to ensure correct selection
                            video_id = video.get('id', f'unknown_{idx}')
                            button_key = f"select_btn_{video_id}"
                            
                            if st.button("✓ Select", key=button_key, width='stretch', type="primary"):
                                # Store the EXACT video that was clicked
                                st.session_state.selected_video_url = video['url']
                                st.session_state.current_input = video['url']
                                st.session_state.hide_search = True  # Flag to hide search results
                                # Force rerun to refresh and hide search results
                                st.rerun()
                        
                        # Divider between results
                        if idx < len(search_results) - 1:
                            st.markdown("<div style='height: 1px; background: linear-gradient(90deg, transparent, #334155, transparent); margin: 1rem 0;'></div>", unsafe_allow_html=True)
                    
                    selected_url = None  # Don't auto-fetch for search results
                else:
                    st.warning("No results found. Try a different search term.")
                    selected_url = None
                    
            elif parsed['type'] == 'invalid_url':
                st.error("❌ Only YouTube URLs are supported")
                selected_url = None
            
            else:
                selected_url = None
        else:
            selected_url = None
        
        # Info box
        with st.expander("💡 How to use"):
            st.markdown("""
                **Three ways to find videos:**
                
                1. **🔍 Search by name**: Type anything like "best music", "funny cats", "tutorial"
                2. **🔗 Paste URL**: Full YouTube URL like `https://youtube.com/watch?v=...`
                3. **🆔 Enter ID**: Just the video ID like `dQw4w9WgXcQ`
                
                **Examples:**
                - `python tutorial for beginners`
                - `https://www.youtube.com/watch?v=dQw4w9WgXcQ`
                - `dQw4w9WgXcQ`
            """)
        
        # Store in session state
        if user_input != st.session_state.get('current_input', ''):
            st.session_state.current_input = user_input
        
        # Return the URL to fetch (if URL or ID was entered)
        if 'selected_video_url' in st.session_state:
            return st.session_state.selected_video_url
        
        return selected_url if selected_url else ''


def render_video_info_card(video_info: Dict):
    """Render video information card"""
    col1, col2 = st.columns([1, 2])
    
    with col1:
        # Display thumbnail with fallback
        thumbnail_url = video_info.get('thumbnail')
        if thumbnail_url and thumbnail_url.strip():
            try:
                st.image(thumbnail_url, width='stretch')
            except Exception as e:
                st.markdown("""
                    <div style="width: 100%; aspect-ratio: 16/9; background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%); 
                    display: flex; align-items: center; justify-content: center; border-radius: 8px; border: 1px solid #334155;">
                        <span style="font-size: 3rem;">🎬</span>
                    </div>
                """, unsafe_allow_html=True)
        else:
            # Placeholder when no thumbnail
            st.markdown("""
                <div style="width: 100%; aspect-ratio: 16/9; background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%); 
                display: flex; align-items: center; justify-content: center; border-radius: 8px; border: 1px solid #334155;">
                    <span style="font-size: 3rem;">🎬</span>
                </div>
            """, unsafe_allow_html=True)
        
        st.markdown(f"""
            <div style="margin-top: 12px; font-size: 13px; color: #cbd5e1; padding: 0.75rem; background-color: #1e293b; border-radius: 8px;">
                <strong>Resolution:</strong> {video_info.get('resolution', 'Various')}<br>
                <strong>Est. Size:</strong> {video_info.get('estimated_size', 'N/A')}
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
            <h2 style="margin: 0 0 8px 0; font-size: 24px; line-height: 1.3;">
                {video_info['title']}
            </h2>
            <div style="color: #94a3b8; font-size: 14px; margin-bottom: 16px;">
                {video_info['uploader']} • {video_info.get('view_count', 0):,} views • {video_info['upload_date']}
            </div>
        """, unsafe_allow_html=True)
        
        stats_cols = st.columns(3)
        with stats_cols[0]:
            st.metric("Duration", video_info['duration_formatted'])
        with stats_cols[1]:
            st.metric("Formats", f"{len(video_info['formats'])} available")
        with stats_cols[2]:
            if video_info.get('like_count'):
                st.metric("Likes", f"{video_info['like_count']:,}")
        
        if video_info.get('description'):
            with st.expander("📄 Description"):
                desc = video_info['description'][:500]
                if len(video_info['description']) > 500:
                    desc += "..."
                st.markdown(desc)
        
        if video_info.get('tags'):
            with st.expander(f"🏷️ Tags ({len(video_info['tags'])})"):
                tags = ' • '.join(video_info['tags'][:15])
                st.markdown(tags)


def render_quick_download(video_info: Dict, settings: SettingsManager):
    """Render quick download options"""
    st.markdown("### Quick Download Options")
    
    # Info box about auto-merge
    st.info("💡 **Auto-Merge Technology**: Best quality videos are automatically combined with best audio for maximum quality (1080p+, 1440p, 4K). Requires FFmpeg.")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
            <div class="custom-card" style="text-align: center; padding: 2rem;">
                <div style="font-size: 3rem; margin-bottom: 1rem;">🎥</div>
                <h3 style="margin-bottom: 0.5rem;">Video</h3>
                <p style="color: #94a3b8; font-size: 0.875rem; margin-bottom: 1.5rem;">
                    Best available quality
                </p>
            </div>
        """, unsafe_allow_html=True)
        
        quality = st.radio(
            "Quality",
            options=['best', 'high', 'medium', 'low'],
            format_func=lambda x: {
                'best': '🌟 Best (1080p+)',
                'high': '⭐ High (1080p)',
                'medium': '✨ Medium (720p)',
                'low': '💫 Low (480p)'
            }[x],
            key="video_quality",
            label_visibility='collapsed'
        )
        
        if st.button("⬇️ Download Video", key="download_video_quick", width='stretch'):
            download_video(video_info, quality, settings)
    
    with col2:
        st.markdown("""
            <div class="custom-card" style="text-align: center; padding: 2rem;">
                <div style="font-size: 3rem; margin-bottom: 1rem;">🎵</div>
                <h3 style="margin-bottom: 0.5rem;">Audio</h3>
                <p style="color: #94a3b8; font-size: 0.875rem; margin-bottom: 1.5rem;">
                    High quality audio extraction
                </p>
            </div>
        """, unsafe_allow_html=True)
        
        audio_format = st.radio(
            "Format",
            options=['mp3', 'm4a', 'opus'],
            format_func=lambda x: {
                'mp3': '🎵 MP3 (320kbps)',
                'm4a': '🎼 M4A (256kbps)',
                'opus': '🎹 Opus (192kbps)',
            }[x],
            key="audio_format",
            label_visibility='collapsed'
        )
        
        if st.button("⬇️ Download Audio", key="download_audio_quick", width='stretch'):
            download_audio(video_info, audio_format, settings)


def render_custom_formats(video_info: Dict, settings: SettingsManager):
    """Render custom format selection"""
    st.markdown("### Available Formats")
    
    processor = FormatProcessor()
    categorized = processor.categorize_formats(video_info['formats'])
    
    # Section 1: Combined Video + Audio (Progressive)
    if categorized['progressive']:
        st.markdown("#### 🎬 Video + Audio (Ready to Play)")
        st.markdown("<p style='color: #94a3b8; font-size: 0.85rem; margin-top: -10px;'>These formats contain both video and audio - no merging needed</p>", unsafe_allow_html=True)
        
        progressive_formats = processor.sort_by_quality(categorized['progressive'], 'video')[:8]
        
        for fmt in progressive_formats:
            col1, col2, col3, col4 = st.columns([3, 2, 2, 1])
            
            with col1:
                resolution = f"{fmt.get('height', '?')}p"
                if fmt.get('fps', 30) > 30:
                    resolution += f"{fmt['fps']}"
                ext = fmt.get('ext', 'unknown').upper()
                st.markdown(f"**{resolution}** <span class='codec-badge'>{ext}</span> <span style='color: #10b981; font-size: 0.75rem;'>✓ Audio Included</span>", unsafe_allow_html=True)
            
            with col2:
                size = fmt.get('filesize') or fmt.get('filesize_approx', 0)
                st.markdown(f"<span class='size-badge'>{FileManager.format_size(size)}</span>", unsafe_allow_html=True)
            
            with col3:
                fps = fmt.get('fps', 'N/A')
                st.markdown(f"<small style='color: #94a3b8;'>FPS: {fps}</small>", unsafe_allow_html=True)
            
            with col4:
                if st.button("⬇️", key=f"dl_prog_{fmt['format_id']}", help="Download - Ready to play"):
                    download_format(video_info, fmt['format_id'], settings, merge_audio=False)
            
            st.markdown("<hr style='margin: 0.5rem 0; opacity: 0.2;'>", unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
    
    # Section 2: Audio Only
    st.markdown("#### 🎵 Audio Only Formats")
    st.markdown("<p style='color: #94a3b8; font-size: 0.85rem; margin-top: -10px;'>Extract audio only - perfect for music and podcasts</p>", unsafe_allow_html=True)
    
    audio_formats = processor.sort_by_quality(categorized['audio_only'], 'audio')[:10]
    
    if audio_formats:
        for fmt in audio_formats:
            col1, col2, col3, col4 = st.columns([3, 2, 2, 1])
            
            with col1:
                codec = fmt.get('acodec', 'unknown')[:15].upper()
                bitrate = fmt.get('abr', 'N/A')
                st.markdown(f"**{codec}** <span class='quality-badge'>{bitrate}kbps</span>", unsafe_allow_html=True)
            
            with col2:
                size = fmt.get('filesize') or fmt.get('filesize_approx', 0)
                st.markdown(f"<span class='size-badge'>{FileManager.format_size(size)}</span>", unsafe_allow_html=True)
            
            with col3:
                sr = fmt.get('asr', 'N/A')
                st.markdown(f"<small style='color: #94a3b8;'>SR: {sr}Hz</small>", unsafe_allow_html=True)
            
            with col4:
                if st.button("⬇️", key=f"dl_audio_{fmt['format_id']}", help="Download audio only"):
                    download_format(video_info, fmt['format_id'], settings, merge_audio=False)
            
            st.markdown("<hr style='margin: 0.5rem 0; opacity: 0.2;'>", unsafe_allow_html=True)
    else:
        st.info("No separate audio formats available.")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Section 3: Video Only (Needs Audio)
    st.markdown("#### 📹 Video Only (No Audio)")
    st.markdown("<p style='color: #f59e0b; font-size: 0.85rem; margin-top: -10px;'>⚠️ These are video-only streams. Audio will be automatically added from best available source.</p>", unsafe_allow_html=True)
    
    video_formats = processor.sort_by_quality(categorized['video_only'], 'video')[:15]
    
    if video_formats:
        for fmt in video_formats:
            col1, col2, col3, col4 = st.columns([3, 2, 2, 1])
            
            with col1:
                resolution = f"{fmt.get('height', '?')}p"
                if fmt.get('fps', 30) > 30:
                    resolution += f"{fmt['fps']}"
                codec = fmt.get('vcodec', 'unknown')[:15]
                st.markdown(f"**{resolution}** <span class='codec-badge'>{codec}</span> <span style='color: #f59e0b; font-size: 0.75rem;'>🔇 No Audio</span>", unsafe_allow_html=True)
            
            with col2:
                size = fmt.get('filesize') or fmt.get('filesize_approx', 0)
                st.markdown(f"<span class='size-badge'>{FileManager.format_size(size)}</span>", unsafe_allow_html=True)
            
            with col3:
                fps = fmt.get('fps', 'N/A')
                st.markdown(f"<small style='color: #94a3b8;'>FPS: {fps}</small>", unsafe_allow_html=True)
            
            with col4:
                if st.button("⬇️", key=f"dl_video_{fmt['format_id']}", help="Download & auto-merge with best audio"):
                    download_format(video_info, fmt['format_id'], settings, merge_audio=True)
            
            st.markdown("<hr style='margin: 0.5rem 0; opacity: 0.2;'>", unsafe_allow_html=True)
    else:
        st.info("No separate video formats available.")


def render_advanced_settings(settings: SettingsManager):
    """Render advanced settings"""
    st.markdown("### Advanced Configuration")
    
    with st.expander("📥 Download Settings", expanded=True):
        col1, col2 = st.columns(2)
        
        with col1:
            save_location = st.text_input(
                "Save Location",
                value=settings.get('download_location'),
                help="Directory where downloads will be saved"
            )
            
            filename_template = st.text_input(
                "Filename Template",
                value=settings.get('filename_template', '{title}'),
                help="Template for downloaded filenames"
            )
        
        with col2:
            concurrent_downloads = st.slider(
                "Concurrent Downloads",
                min_value=1,
                max_value=10,
                value=settings.get('concurrent_downloads', 3)
            )
            
            retry_attempts = st.slider(
                "Retry Attempts",
                min_value=1,
                max_value=10,
                value=settings.get('retry_attempts', 3)
            )
    
    with st.expander("🔧 Post-Processing"):
        col1, col2 = st.columns(2)
        
        with col1:
            embed_thumbnail = st.checkbox(
                "Embed Thumbnail",
                value=settings.get('embed_thumbnail', True)
            )
            
            embed_metadata = st.checkbox(
                "Embed Metadata",
                value=settings.get('embed_metadata', True)
            )
        
        with col2:
            auto_convert = st.checkbox(
                "Auto Convert to MP4",
                value=settings.get('auto_convert', False)
            )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("💾 Save Settings", width='stretch'):
            settings.set('download_location', save_location)
            settings.set('filename_template', filename_template)
            settings.set('concurrent_downloads', concurrent_downloads)
            settings.set('retry_attempts', retry_attempts)
            settings.set('embed_thumbnail', embed_thumbnail)
            settings.set('embed_metadata', embed_metadata)
            settings.set('auto_convert', auto_convert)
            
            settings.save_settings()
            st.success("✅ Settings saved successfully!")
    
    with col2:
        if st.button("↻ Reset to Defaults", width='stretch'):
            settings.reset_to_defaults()
            st.success("✅ Settings reset!")
            st.rerun()


def render_batch_download():
    """Render batch download interface"""
    st.markdown("### Batch Download")
    
    st.markdown("**Paste multiple URLs (one per line)**")
    urls_text = st.text_area(
        "URLs",
        height=200,
        placeholder="https://youtube.com/watch?v=...\nhttps://vimeo.com/...\n",
        label_visibility='collapsed'
    )
    
    if st.button("📋 Process Batch", key="process_batch"):
        if urls_text.strip():
            urls = [line.strip() for line in urls_text.split('\n') if line.strip()]
            st.info(f"Found {len(urls)} URLs. Batch processing coming soon!")
        else:
            st.warning("Please enter at least one URL")


def render_footer():
    """Render footer"""
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.divider()
    
    st.markdown(f"""
        <div style="text-align: center; padding: 1rem; color: #64748b;">
            <p style="margin: 0.5rem 0;">
                <strong style="color: #94a3b8;">Converso Downloader</strong> v{__version__}
            </p>
            <p style="margin: 0.5rem 0; font-size: 0.875rem;">
                Powered by yt-dlp • FFmpeg • Streamlit
            </p>
            <p style="margin: 0.5rem 0; font-size: 0.875rem;">
                Created by <strong><a href="https://github.com/Converso-Empire" target="_blank" style="color: #3b82f6; text-decoration: none;">Converso Empire</a></strong>
            </p>
            <p style="margin-top: 1rem; font-size: 0.75rem; color: #475569;">
                {__copyright__}<br>
                All Converso Empire projects are protected under the Converso Empire License (CEL).<br>
                Unauthorized reproduction or redistribution is strictly prohibited.
            </p>
        </div>
    """, unsafe_allow_html=True)


# Download helper functions

def download_video(video_info: Dict, quality: str, settings: SettingsManager):
    """Download video with specified quality - automatically merges with best audio"""
    processor = FormatProcessor()
    format_id = processor.get_best_format_id(video_info['formats'], quality)
    
    if not format_id:
        st.error("❌ No suitable format found")
        return
    
    download_path = settings.get('download_location')
    
    progress_placeholder = st.empty()
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    def progress_callback(info):
        if info['status'] == 'downloading':
            percent = info.get('percent', 0)
            speed = info.get('speed', 0)
            
            progress_bar.progress(min(int(percent), 100) / 100)
            status_text.text(f"Downloading: {percent:.1f}% • Speed: {FileManager.format_size(speed)}/s")
        elif info['status'] == 'finished':
            status_text.text("Merging video and audio... (requires FFmpeg)")
    
    downloader = VideoDownloader(download_path, progress_callback)
    
    with st.spinner("Starting download..."):
        # Automatically merge with best audio for highest quality
        result = downloader.download(
            video_info['webpage_url'],
            format_id + '+bestaudio',
            {
                'embed_thumbnail': settings.get('embed_thumbnail'),
                'embed_metadata': settings.get('embed_metadata'),
                'merge_output_format': 'mp4',
            }
        )
    
    progress_bar.progress(100)
    
    if result['success']:
        st.success(f"✅ Downloaded: {result['title']}")
        st.info(f"📁 Saved to: {result['filepath']}")
    else:
        st.error(f"❌ Download failed: {result.get('error', 'Unknown error')}")


def download_audio(video_info: Dict, audio_format: str, settings: SettingsManager):
    """Download audio only"""
    download_path = settings.get('download_location')
    
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    def progress_callback(info):
        if info['status'] == 'downloading':
            percent = info.get('percent', 0)
            progress_bar.progress(min(int(percent), 100) / 100)
            status_text.text(f"Downloading: {percent:.1f}%")
    
    downloader = VideoDownloader(download_path, progress_callback)
    
    with st.spinner("Extracting audio..."):
        result = downloader.download(
            video_info['webpage_url'],
            'bestaudio',
            {
                'extract_audio': True,
                'audio_format': audio_format,
                'audio_quality': '320' if audio_format == 'mp3' else '192',
            }
        )
    
    if result['success']:
        st.success(f"✅ Downloaded audio: {result['title']}")
        st.info(f"📁 Saved to: {result['filepath']}")
    else:
        st.error(f"❌ Download failed: {result.get('error', 'Unknown error')}")


def download_format(video_info: Dict, format_id: str, settings: SettingsManager, merge_audio: bool = False):
    """Download specific format with optional audio merging"""
    download_path = settings.get('download_location')
    
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    def progress_callback(info):
        if info['status'] == 'downloading':
            percent = info.get('percent', 0)
            speed = info.get('speed', 0)
            progress_bar.progress(min(int(percent), 100) / 100)
            status_text.text(f"Downloading: {percent:.1f}% • Speed: {FileManager.format_size(speed)}/s")
        elif info['status'] == 'finished':
            if merge_audio:
                status_text.text("Merging video and audio... (requires FFmpeg)")
    
    downloader = VideoDownloader(download_path, progress_callback)
    
    # If merging audio, add bestaudio to format for highest quality
    if merge_audio:
        format_id = format_id + '+bestaudio'
        status_message = "Downloading and merging with best audio..."
    else:
        status_message = "Downloading..."
    
    with st.spinner(status_message):
        result = downloader.download(
            video_info['webpage_url'],
            format_id,
            {
                'embed_thumbnail': settings.get('embed_thumbnail'),
                'embed_metadata': settings.get('embed_metadata'),
                'merge_output_format': 'mp4' if merge_audio else None,
            }
        )
    
    progress_bar.progress(100)
    
    if result['success']:
        if merge_audio:
            st.success(f"✅ Downloaded & Merged: {result['title']}")
        else:
            st.success(f"✅ Downloaded: {result['title']}")
        st.info(f"📁 Saved to: {result['filepath']}")
    else:
        st.error(f"❌ Download failed: {result.get('error', 'Unknown error')}")
