"""File utility functions for Converso Pro Downloader"""

import os
import json
from pathlib import Path
from typing import Dict, Optional


class FileManager:
    """Manage file operations"""
    
    @staticmethod
    def ensure_directory(path: str) -> bool:
        """Ensure directory exists, create if not"""
        try:
            Path(path).mkdir(parents=True, exist_ok=True)
            return True
        except Exception as e:
            print(f"Error creating directory: {e}")
            return False
    
    @staticmethod
    def get_unique_filename(filepath: str) -> str:
        """
        Get unique filename by appending number if file exists
        e.g., video.mp4 -> video (1).mp4 -> video (2).mp4
        """
        if not os.path.exists(filepath):
            return filepath
        
        directory = os.path.dirname(filepath)
        filename = os.path.basename(filepath)
        name, ext = os.path.splitext(filename)
        
        counter = 1
        while True:
            new_filename = f"{name} ({counter}){ext}"
            new_filepath = os.path.join(directory, new_filename)
            if not os.path.exists(new_filepath):
                return new_filepath
            counter += 1
    
    @staticmethod
    def get_file_size(filepath: str) -> int:
        """Get file size in bytes"""
        try:
            return os.path.getsize(filepath)
        except Exception:
            return 0
    
    @staticmethod
    def delete_file(filepath: str) -> bool:
        """Safely delete a file"""
        try:
            if os.path.exists(filepath):
                os.remove(filepath)
                return True
            return False
        except Exception as e:
            print(f"Error deleting file: {e}")
            return False
    
    @staticmethod
    def format_size(bytes_size: int) -> str:
        """Format bytes to human-readable size"""
        if not bytes_size or bytes_size <= 0:
            return "Unknown"
        
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if bytes_size < 1024.0:
                return f"{bytes_size:.1f} {unit}"
            bytes_size /= 1024.0
        return f"{bytes_size:.1f} PB"
    
    @staticmethod
    def format_duration(seconds: float) -> str:
        """Format seconds to HH:MM:SS or MM:SS"""
        if not seconds or seconds <= 0:
            return "Unknown"
        
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        secs = int(seconds % 60)
        
        if hours > 0:
            return f"{hours}:{minutes:02d}:{secs:02d}"
        return f"{minutes}:{secs:02d}"


class ConfigManager:
    """Manage application configuration"""
    
    def __init__(self, config_path: Optional[str] = None):
        if config_path:
            self.config_path = Path(config_path)
        else:
            # Use user's home directory
            self.config_path = Path.home() / '.converso' / 'config.json'
        
        self.config_path.parent.mkdir(parents=True, exist_ok=True)
    
    def load_config(self) -> Dict:
        """Load configuration from file"""
        try:
            if self.config_path.exists():
                with open(self.config_path, 'r', encoding='utf-8') as f:
                    return json.load(f)
        except Exception as e:
            print(f"Error loading config: {e}")
        
        return self.get_default_config()
    
    def save_config(self, config: Dict) -> bool:
        """Save configuration to file"""
        try:
            with open(self.config_path, 'w', encoding='utf-8') as f:
                json.dump(config, f, indent=2)
            return True
        except Exception as e:
            print(f"Error saving config: {e}")
            return False
    
    @staticmethod
    def get_default_config() -> Dict:
        """Get default configuration"""
        return {
            'download_location': str(Path.home() / 'Downloads' / 'Converso'),
            'quality_preference': 'best',
            'output_format': 'mp4',
            'concurrent_downloads': 3,
            'embed_thumbnail': True,
            'embed_metadata': True,
            'theme': 'dark',
            'notifications_enabled': True,
            'keep_history_days': 30,
            'filename_template': '{title}_{resolution}',
            'audio_bitrate': '192k',
            'download_subtitles': False,
            'subtitle_languages': ['en'],
            'retry_attempts': 3,
            'timeout': 30
        }
