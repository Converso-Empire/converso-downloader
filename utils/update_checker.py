"""
Update Checker for Converso Downloader
Checks for new releases on GitHub and notifies users
© 2025 Converso Empire. All rights reserved.
"""

import requests
from packaging import version
from typing import Optional, Dict, Tuple
import logging

logger = logging.getLogger(__name__)


class UpdateChecker:
    """Checks for application updates from GitHub releases"""
    
    def __init__(self, current_version: str, repo_url: str):
        """
        Initialize update checker
        
        Args:
            current_version: Current application version (e.g., "2.1.4")
            repo_url: GitHub repository URL
        """
        self.current_version = current_version
        self.repo_url = repo_url
        
        # Extract owner and repo name from URL
        # Expected format: https://github.com/owner/repo
        parts = repo_url.rstrip('/').split('/')
        self.owner = parts[-2]
        self.repo = parts[-1]
        
        self.api_url = f"https://api.github.com/repos/{self.owner}/{self.repo}/releases/latest"
    
    def check_for_updates(self, timeout: int = 5) -> Tuple[bool, Optional[Dict]]:
        """
        Check if a new version is available
        
        Args:
            timeout: Request timeout in seconds
            
        Returns:
            Tuple of (update_available: bool, release_info: dict or None)
        """
        try:
            response = requests.get(self.api_url, timeout=timeout)
            response.raise_for_status()
            
            release_data = response.json()
            latest_version = release_data.get('tag_name', '').lstrip('v')
            
            if not latest_version:
                logger.warning("Could not determine latest version from GitHub")
                return False, None
            
            # Compare versions
            if version.parse(latest_version) > version.parse(self.current_version):
                return True, {
                    'version': latest_version,
                    'tag_name': release_data.get('tag_name', ''),
                    'release_name': release_data.get('name', ''),
                    'release_notes': release_data.get('body', ''),
                    'download_url': release_data.get('html_url', ''),
                    'published_at': release_data.get('published_at', ''),
                    'assets': release_data.get('assets', [])
                }
            
            return False, None
            
        except requests.RequestException as e:
            logger.warning(f"Failed to check for updates: {e}")
            return False, None
        except Exception as e:
            logger.error(f"Unexpected error checking for updates: {e}")
            return False, None
    
    def get_download_url(self, release_info: Dict, platform: str = 'windows') -> Optional[str]:
        """
        Get the download URL for a specific platform
        
        Args:
            release_info: Release information dictionary
            platform: Platform name ('windows', 'linux', 'macos')
            
        Returns:
            Download URL or None
        """
        assets = release_info.get('assets', [])
        
        # Platform-specific patterns
        patterns = {
            'windows': ['windows', 'win', '.exe', '.zip'],
            'linux': ['linux', 'ubuntu'],
            'macos': ['macos', 'mac', 'darwin']
        }
        
        platform_patterns = patterns.get(platform.lower(), [])
        
        # Find matching asset
        for asset in assets:
            asset_name = asset.get('name', '').lower()
            if any(pattern in asset_name for pattern in platform_patterns):
                return asset.get('browser_download_url')
        
        # Fallback to release page
        return release_info.get('download_url')
    
    def format_update_message(self, release_info: Dict) -> str:
        """
        Format a user-friendly update notification message
        
        Args:
            release_info: Release information dictionary
            
        Returns:
            Formatted message string
        """
        version = release_info.get('version', 'Unknown')
        release_name = release_info.get('release_name', '')
        
        message = f"🎉 **New Version Available: v{version}**\n\n"
        
        if release_name:
            message += f"**{release_name}**\n\n"
        
        message += f"Current version: v{self.current_version}\n"
        message += f"Latest version: v{version}\n\n"
        
        release_notes = release_info.get('release_notes', '')
        if release_notes:
            # Truncate long release notes
            if len(release_notes) > 500:
                release_notes = release_notes[:500] + "..."
            message += f"**What's New:**\n{release_notes}\n\n"
        
        download_url = release_info.get('download_url', '')
        if download_url:
            message += f"[Download Latest Version]({download_url})"
        
        return message
