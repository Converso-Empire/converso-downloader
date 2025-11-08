# -*- mode: python ; coding: utf-8 -*-
"""
PyInstaller spec file for Converso Downloader
Builds standalone executable with all dependencies
"""

from PyInstaller.utils.hooks import collect_data_files, collect_submodules
import sys
import os

block_cipher = None

# Collect all necessary data files
datas = []
datas += collect_data_files('streamlit')
datas += collect_data_files('streamlit_option_menu', include_py_files=True)
datas += collect_data_files('altair')
datas += collect_data_files('validators')

# Add project directories
datas += [('config', 'config')]
datas += [('utils', 'utils')]
datas += [('version.py', '.')]

# Collect hidden imports
hiddenimports = []
hiddenimports += collect_submodules('streamlit')
hiddenimports += collect_submodules('yt_dlp')
hiddenimports += ['validators', 'altair', 'watchdog']
hiddenimports += ['urllib3', 'certifi', 'chardet', 'idna']
hiddenimports += ['brotli', 'pycryptodomex', 'websockets', 'mutagen']

a = Analysis(
    ['app.py'],
    pathex=[],
    binaries=[],
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['matplotlib', 'numpy', 'pandas', 'scipy'],  # Exclude unused heavy packages
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
    console=True,  # Show console for error messages
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=icon_path,
)
