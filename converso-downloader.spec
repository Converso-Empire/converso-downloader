# -*- mode: python ; coding: utf-8 -*-
"""
PyInstaller spec file for Converso Downloader
Builds standalone executable with all dependencies
"""

from PyInstaller.utils.hooks import collect_data_files, collect_submodules, copy_metadata
import sys
import os

block_cipher = None

# Helper function to safely copy metadata
def safe_copy_metadata(package_name):
    """Safely copy package metadata, ignoring if not found"""
    try:
        return copy_metadata(package_name)
    except Exception as e:
        print(f"Warning: Could not collect metadata for {package_name}: {e}")
        return []

# Collect all necessary data files
datas = []
datas += collect_data_files('streamlit')
datas += collect_data_files('streamlit_option_menu', include_py_files=True)
datas += collect_data_files('altair')

# Collect package metadata (required for importlib.metadata)
# Only collect metadata for packages that have it
datas += safe_copy_metadata('streamlit')
datas += safe_copy_metadata('altair')
datas += safe_copy_metadata('yt-dlp')
datas += safe_copy_metadata('Pillow')
datas += safe_copy_metadata('requests')
datas += safe_copy_metadata('packaging')
datas += safe_copy_metadata('streamlit-option-menu')  # Try with dash instead of underscore

# Add project directories and files
datas += [('config', 'config')]
datas += [('utils', 'utils')]
datas += [('version.py', '.')]
datas += [('app.py', '.')]  # Main app file
datas += [('ui_components.py', '.')]  # UI components file

# Collect hidden imports
hiddenimports = []
hiddenimports += collect_submodules('streamlit')
hiddenimports += collect_submodules('yt_dlp')
hiddenimports += ['validators', 'altair', 'watchdog']
hiddenimports += ['urllib3', 'certifi', 'chardet', 'idna']
hiddenimports += ['brotli', 'pycryptodomex', 'websockets', 'mutagen']

a = Analysis(
    ['launcher.py'],  # Use launcher instead of app.py directly
    pathex=[],
    binaries=[],
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['matplotlib', 'pandas', 'scipy'],  # Exclude unused heavy packages (keep numpy for streamlit)
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

# Conditionally set icon if it exists
icon_path = 'assets/icon.ico' if sys.platform == 'win32' and os.path.exists('assets/icon.ico') else None

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='ConversoDownloader',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,  # Hide console for better user experience (Streamlit will open browser)
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=icon_path,
)
