"""
Version information for Converso Downloader
© 2025 Converso Empire. All rights reserved.
"""

__version__ = "2.1.3"
__app_name__ = "Converso Downloader"
__description__ = "Professional YouTube Downloader with Smart Search"
__author__ = "Converso Empire"
__github__ = "https://github.com/Converso-Empire"
__repo__ = "https://github.com/Converso-Empire/converso-downloader"
__build_date__ = "2024-11"

# Version components
VERSION_MAJOR = 2
VERSION_MINOR = 1
VERSION_PATCH = 3

# Build information
BUILD_TYPE = "Production"
BUILD_STATUS = "Stable"

# License
__license__ = "Converso Empire License (CEL)"
__copyright__ = "© 2025 Converso Empire. All rights reserved."

def get_version_string():
    """Get formatted version string"""
    return f"v{__version__}"

def get_full_version_info():
    """Get complete version information"""
    return {
        "version": __version__,
        "app_name": __app_name__,
        "description": __description__,
        "build_type": BUILD_TYPE,
        "build_status": BUILD_STATUS,
        "build_date": __build_date__
    }
