# Changelog

All notable changes to Converso Downloader will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.1.4] - 2025-11-08

### Fixed
- **Critical:** Fixed `importlib.metadata.PackageNotFoundError` in PyInstaller builds
  - Added metadata collection for Streamlit and all dependencies in the .spec file
  - Users can now run the Windows executable without metadata errors
  - Added safe metadata collection to handle packages without metadata
- **Critical:** Fixed session state initialization errors when running executable
  - Created proper launcher script to run Streamlit correctly
  - Added safe session state access using `.get()` method
  - Executable now launches properly without session state errors
- **Critical:** Fixed development mode assertion error in production
  - Created `streamlit_config.toml` with production-ready settings
  - Disabled development mode globally (`global.developmentMode=false`)
  - Configured launcher to use production settings via environment variables
  - Disabled unnecessary security features (CORS/XSRF) for local desktop use
- Fixed dependency conflict with `packaging` library version
  - Changed to `packaging<24,>=16.8` to match Streamlit's requirements
- Fixed PyInstaller build error for packages without metadata (validators)
  - Implemented `safe_copy_metadata()` helper function to gracefully skip packages without metadata

### Added
- **Automatic Update Checker:** Application now checks for new releases on startup
  - Notifies users when a new version is available
  - Displays release notes and download links
  - Non-intrusive notification that doesn't block usage
- New `utils/update_checker.py` module for GitHub release checking
- Added `packaging` library dependency for version comparison (compatible with Streamlit)

### Changed
- Updated PyInstaller spec file with comprehensive metadata collection
- Enhanced session state to track update checking status
- Changed entry point from `app.py` to `launcher.py` for proper Streamlit initialization
- Disabled console window for better user experience (Streamlit opens in browser automatically)
- Improved error handling and session state initialization to prevent crashes
- Configured Streamlit for production mode with optimized settings:
  - Disabled development mode warnings
  - Minimized logging (error level only)
  - Disabled usage statistics collection
  - Optimized toolbar display

---

## [2.1.3] - 2025-11

### Added
- Initial public release
- Professional YouTube downloader with smart search
- Multiple format support (MP4, WebM, MP3, M4A, WAV)
- Batch download capability
- Custom format selection
- Advanced settings and preferences
- Cross-platform support (Windows, Linux, macOS)

---

## Release Notes

### How to Update
1. Download the latest release from [GitHub Releases](https://github.com/Converso-Empire/converso-downloader/releases)
2. Extract the archive
3. Run `ConversoDownloader.exe` (Windows) or `ConversoDownloader` (Linux/macOS)

### Support
For issues, bug reports, or feature requests, please visit:
- [GitHub Issues](https://github.com/Converso-Empire/converso-downloader/issues)
- [Documentation](https://github.com/Converso-Empire/converso-downloader/blob/main/README.md)
