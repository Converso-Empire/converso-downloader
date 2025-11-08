# Release Instructions for v2.1.4

## Pre-Release Checklist

- [x] Version updated to 2.1.4 in `version.py`
- [x] `CHANGELOG.md` updated with release notes
- [x] All code changes committed
- [x] PyInstaller spec file updated with metadata fixes
- [x] Update checker implemented and tested
- [ ] Local build tested successfully
- [ ] All tests passing (if applicable)

## Step 1: Build and Test Locally

### Install/Update Dependencies
```powershell
pip install -r requirements.txt
pip install pyinstaller
```

### Build the Executable
```powershell
pyinstaller converso-downloader.spec
```

### Test the Build
```powershell
# Run the executable
.\dist\ConversoDownloader.exe

# Verify:
# - Application starts without errors
# - Version shows as 2.1.4
# - Update checker works (may show no update available yet)
# - All features work correctly
```

## Step 2: Commit and Tag

### Commit All Changes
```powershell
git add .
git commit -m "Release v2.1.4: Fix metadata error and add update checker"
```

### Create and Push Tag
```powershell
# Create annotated tag
git tag -a v2.1.4 -m "Release v2.1.4

Fixes:
- Fixed importlib.metadata.PackageNotFoundError in PyInstaller builds

Features:
- Added automatic update checker
- Notifies users of new releases on startup

Changes:
- Enhanced PyInstaller spec with comprehensive metadata collection
- Added packaging library for version comparison"

# Push commits and tags
git push origin main
git push origin v2.1.4
```

## Step 3: GitHub Actions

The GitHub Actions workflow will automatically:
1. Trigger on the `v2.1.4` tag
2. Build executables for Windows, Linux, and macOS
3. Create a GitHub release
4. Upload the built executables as release assets

### Monitor the Build
1. Go to: https://github.com/Converso-Empire/converso-downloader/actions
2. Watch the "Build and Release" workflow
3. Ensure all builds complete successfully

## Step 4: Verify Release

### After GitHub Actions Completes
1. Go to: https://github.com/Converso-Empire/converso-downloader/releases
2. Verify the v2.1.4 release was created
3. Check that all platform executables are attached
4. Download and test the Windows executable
5. Verify the update checker works in v2.1.3 (should detect v2.1.4)

## Step 5: Update Release Notes (Optional)

If you want to enhance the auto-generated release notes:
1. Edit the v2.1.4 release on GitHub
2. Add additional context or screenshots
3. Save the updated release

## Release Announcement Template

```markdown
# 🎉 Converso Downloader v2.1.4 Released!

## What's Fixed
- **Critical Bug Fix:** Resolved the `importlib.metadata.PackageNotFoundError` that prevented the Windows executable from running
- Users who downloaded v2.1.3 can now upgrade to v2.1.4 for a working executable

## What's New
- **Automatic Update Checker:** The app now checks for new releases and notifies you when updates are available
- Non-intrusive notification with release notes and download links
- Stay up-to-date with the latest features and fixes

## Download
- [Windows](https://github.com/Converso-Empire/converso-downloader/releases/download/v2.1.4/Converso-Downloader-Windows.zip)
- [Linux](https://github.com/Converso-Empire/converso-downloader/releases/download/v2.1.4/Converso-Downloader-Linux.tar.gz)
- [macOS](https://github.com/Converso-Empire/converso-downloader/releases/download/v2.1.4/Converso-Downloader-macOS.tar.gz)

## Installation
1. Download the appropriate file for your platform
2. Extract the archive
3. Run `ConversoDownloader.exe` (Windows) or `ConversoDownloader` (Linux/macOS)

Full changelog: [CHANGELOG.md](https://github.com/Converso-Empire/converso-downloader/blob/main/CHANGELOG.md)
```

## Troubleshooting

### If the Build Fails
- Check the GitHub Actions logs for errors
- Ensure all dependencies are in `requirements.txt`
- Verify the `.spec` file has no syntax errors
- Test the build locally first

### If the Tag Needs to be Recreated
```powershell
# Delete local tag
git tag -d v2.1.4

# Delete remote tag
git push origin :refs/tags/v2.1.4

# Create new tag and push
git tag -a v2.1.4 -m "Your message"
git push origin v2.1.4
```

## Post-Release

- [ ] Verify downloads work from GitHub releases
- [ ] Test update checker with v2.1.3 → v2.1.4 upgrade
- [ ] Monitor issue tracker for any problems
- [ ] Update documentation if needed
