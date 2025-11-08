"""URL validation and input validators for Converso Pro Downloader"""

import re
from urllib.parse import urlparse


class URLValidator:
    """Validate and parse YouTube URLs, IDs, and search queries"""
    
    @staticmethod
    def is_valid_url(url: str) -> tuple[bool, str]:
        """
        Validate if the input is a valid YouTube URL, ID, or can be used as search
        Returns: (is_valid, error_message)
        """
        if not url or not url.strip():
            return False, "Input cannot be empty"
        
        url = url.strip()
        
        # If it's a URL, check if it's YouTube
        if url.startswith('http://') or url.startswith('https://'):
            youtube_domains = ['youtube.com', 'youtu.be', 'm.youtube.com', 'www.youtube.com']
            if any(domain in url.lower() for domain in youtube_domains):
                return True, ""
            else:
                return False, "Only YouTube URLs are supported"
        
        # If it's 11 characters, likely a video ID
        if len(url) == 11 and url.isalnum():
            return True, ""
        
        # Otherwise treat as search query (always valid for non-URLs)
        return True, ""
    
    @staticmethod
    def extract_video_id(url: str, platform: str = 'youtube') -> str:
        """Extract video ID from URL"""
        if platform == 'youtube':
            patterns = [
                r'(?:v=|\/)([0-9A-Za-z_-]{11}).*',
                r'(?:embed\/)([0-9A-Za-z_-]{11})',
                r'(?:watch\?v=)([0-9A-Za-z_-]{11})'
            ]
            for pattern in patterns:
                match = re.search(pattern, url)
                if match:
                    return match.group(1)
        
        return ""
    
    @staticmethod
    def is_playlist_url(url: str) -> bool:
        """Check if URL is a playlist"""
        playlist_indicators = ['playlist', 'list=', '/sets/', '/album/']
        return any(indicator in url.lower() for indicator in playlist_indicators)
    
    @staticmethod
    def is_channel_url(url: str) -> bool:
        """Check if URL is a channel"""
        channel_indicators = ['/channel/', '/user/', '/c/', '/@']
        return any(indicator in url.lower() for indicator in channel_indicators)


class FileValidator:
    """Validate file paths and names"""
    
    INVALID_CHARS = r'[<>:"/\\|?*]'
    
    @staticmethod
    def sanitize_filename(filename: str, max_length: int = 200) -> str:
        """
        Sanitize filename by removing invalid characters
        """
        # Remove invalid characters
        filename = re.sub(FileValidator.INVALID_CHARS, '_', filename)
        
        # Remove leading/trailing spaces and dots
        filename = filename.strip('. ')
        
        # Truncate if too long
        if len(filename) > max_length:
            name, ext = filename.rsplit('.', 1) if '.' in filename else (filename, '')
            max_name_length = max_length - len(ext) - 1
            filename = name[:max_name_length] + ('.' + ext if ext else '')
        
        return filename
    
    @staticmethod
    def is_valid_path(path: str) -> bool:
        """Check if path is valid"""
        import os
        try:
            # Check if path is absolute and exists or can be created
            return os.path.isabs(path) or len(path) > 0
        except Exception:
            return False
