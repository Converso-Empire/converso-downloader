"""Settings manager for Converso Pro Downloader"""

import json
from pathlib import Path
from typing import Dict, Any, Optional


class SettingsManager:
    """Manage application settings with persistence"""
    
    def __init__(self, config_path: Optional[str] = None):
        if config_path:
            self.config_path = Path(config_path)
        else:
            # Use user's home directory
            self.config_path = Path.home() / '.converso' / 'settings.json'
        
        self.config_path.parent.mkdir(parents=True, exist_ok=True)
        self.settings = self.load_settings()
    
    def load_settings(self) -> Dict:
        """Load settings from file or use defaults"""
        try:
            if self.config_path.exists():
                with open(self.config_path, 'r', encoding='utf-8') as f:
                    loaded = json.load(f)
                    # Merge with defaults to ensure all keys exist
                    defaults = self.get_default_settings()
                    defaults.update(loaded)
                    return defaults
        except Exception as e:
            print(f"Error loading settings: {e}")
        
        return self.get_default_settings()
    
    def save_settings(self) -> bool:
        """Save current settings to file"""
        try:
            with open(self.config_path, 'w', encoding='utf-8') as f:
                json.dump(self.settings, f, indent=2)
            return True
        except Exception as e:
            print(f"Error saving settings: {e}")
            return False
    
    def get(self, key: str, default: Any = None) -> Any:
        """Get setting value"""
        return self.settings.get(key, default)
    
    def set(self, key: str, value: Any):
        """Set setting value"""
        self.settings[key] = value
    
    def reset_to_defaults(self):
        """Reset all settings to defaults"""
        self.settings = self.get_default_settings()
        self.save_settings()
    
    @staticmethod
    def get_default_settings() -> Dict:
        """Get default settings dictionary"""
        return {
            'download_location': str(Path.home() / 'Downloads' / 'Converso'),
            'quality_preference': 'best',
            'output_format': 'mp4',
            'concurrent_downloads': 3,
            'embed_thumbnail': True,
            'embed_metadata': True,
            'embed_chapters': False,
            'theme': 'dark',
            'notifications_enabled': True,
            'keep_history_days': 30,
            'filename_template': '{title}_{resolution}',
            'audio_bitrate': '192k',
            'download_subtitles': False,
            'subtitle_languages': ['en'],
            'subtitle_format': 'srt',
            'retry_attempts': 3,
            'timeout': 30,
            'speed_limit': 'unlimited',
            'auto_convert': False,
            'extract_audio_copy': False,
            'normalize_audio': False,
            'add_to_library': False,
        }
