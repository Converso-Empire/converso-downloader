# 🎬 Converso Downloader

<div align="center">

**Professional YouTube Downloader with Smart Search**

[![Version](https://img.shields.io/badge/version-2.1.3-blue)](https://github.com/Converso-Empire/converso-downloader/releases)
[![Platform](https://img.shields.io/badge/platform-YouTube-red)](https://youtube.com)
[![License](https://img.shields.io/badge/license-CEL-orange)](https://github.com/Converso-Empire)
[![Made by](https://img.shields.io/badge/Made%20by-Converso%20Empire-blueviolet)](https://github.com/Converso-Empire)

**Created by [Converso Empire](https://github.com/Converso-Empire)**

[Download Latest Release](https://github.com/Converso-Empire/converso-downloader/releases/latest) • [Report Bug](https://github.com/Converso-Empire/converso-downloader/issues) • [Request Feature](https://github.com/Converso-Empire/converso-downloader/issues)

</div>

---

## 🚀 Quick Start

### Download Pre-Built Executable (Recommended)

**✅ No Installation Required • FFmpeg Included • Ready to Use**

1. **Download** the latest release for your platform:
   - [Windows (64-bit)](https://github.com/Converso-Empire/converso-downloader/releases/latest) - `Converso-Downloader-Windows.zip`
   - [macOS (Intel/Apple Silicon)](https://github.com/Converso-Empire/converso-downloader/releases/latest) - `Converso-Downloader-macOS.tar.gz`
   - [Linux (64-bit)](https://github.com/Converso-Empire/converso-downloader/releases/latest) - `Converso-Downloader-Linux.tar.gz`

2. **Extract** the downloaded file

3. **Run** the application:
   - **Windows**: Double-click `ConversoDownloader.exe`
   - **macOS/Linux**: Run `./ConversoDownloader` in terminal

4. **Done!** The app opens automatically in your browser

> **✨ FFmpeg is included!** No separate installation needed.

---

## ✨ Features

### Core Functionality
- 🔍 **Smart YouTube Search**: Search videos by name, paste URLs, or enter video IDs
- ⚡ **Real-Time Search Results**: See search results instantly with thumbnails and details
- 🎯 **Multiple Input Methods**: URL, video ID, or natural search queries
- ⚡ **Auto-Merge Highest Quality**: Automatically combines best video and audio streams for maximum quality (1080p, 1440p, 4K, 8K)
- 📋 **Batch Downloads**: Process multiple URLs at once
- 🎵 **Audio Extraction**: Extract high-quality audio in MP3, M4A, or Opus formats
- 📝 **Subtitle Support**: Download and embed subtitles in multiple languages
- 🔄 **Format Conversion**: Convert videos to MP4, MKV, or WebM
- 💾 **Post-Processing**: Embed thumbnails, metadata, and chapters

### User Experience
- 🎨 **Modern Dark Theme**: Professional, minimalist design
- 🔍 **Intelligent Search**: Search YouTube directly from the app
- ⚡ **Real-Time Results**: See search results as you type
- 📊 **Format Preview**: View all available formats before downloading
- 💼 **Advanced Settings**: Fine-tune every aspect of downloads
- 🎯 **Quality Presets**: One-click downloads with smart defaults
- 📱 **Intuitive Interface**: Easy to use for beginners, powerful for experts

---

## 🛠 Technology Stack

- **Frontend**: Streamlit (Modern web UI framework)
- **Backend**: Python 3.8+
- **Download Engine**: yt-dlp (Universal video downloader)
- **Media Processing**: FFmpeg (Audio/video processing)
- **UI Design**: Custom CSS with Inter font family

---

## 📋 Requirements

### System Requirements
- **Python**: 3.8 or higher
- **FFmpeg**: Required for audio extraction and video merging
- **OS**: Windows, macOS, or Linux

### Python Dependencies
```
streamlit==1.32.0
yt-dlp==2024.3.10
Pillow==10.2.0
requests==2.31.0
python-dateutil==2.8.2
```

---

## 💻 Running from Source (For Developers)

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation

```bash
# Clone the repository
git clone https://github.com/Converso-Empire/converso-downloader.git
cd converso-downloader

# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run app.py
```

**Or use the run scripts:**
- Windows: `run.bat`
- macOS/Linux: `./run.sh`

### Install FFmpeg (Required for source)

#### Windows
1. Download FFmpeg from [ffmpeg.org](https://ffmpeg.org/download.html)
2. Extract the files
3. Add the `bin` folder to your System PATH
4. Verify installation: `ffmpeg -version`

#### macOS
```bash
brew install ffmpeg
```

#### Linux (Ubuntu/Debian)
```bash
sudo apt-get update
sudo apt-get install ffmpeg
```

#### Linux (Fedora)
```bash
sudo dnf install ffmpeg
```

### Step 3: Verify Installation

```bash
# Check Python version
python --version

# Check FFmpeg installation
ffmpeg -version

# Check yt-dlp
yt-dlp --version
```

---

## 🎯 Usage

### Starting the Application

```bash
# Navigate to project directory
cd converso-downloader

# Run the application
streamlit run app.py
```

The application will automatically open in your default web browser at `http://localhost:8501`

---

## 📖 How to Use

### Simple 3-Step Process

**1. Find Your Video**
- 🔍 **Search by Name**: Type "best music 2024" or any video name
- 🔗 **Paste URL**: Any YouTube URL
- 🆔 **Enter Video ID**: Just the 11-character ID

**2. Select & Configure**
- Click "✓ Select" on search results
- Choose quality preset (Best, High, Medium, Low)
- Or select custom format for advanced control

**3. Download**
- Click "⬇️ Download Video" or "⬇️ Download Audio"
- Watch real-time progress
- Done! Files saved to your Downloads folder

---

## 📖 Feature Guide

### Quick Download Tab

Perfect for everyday use with smart defaults:

- **Video Download**: 
  - Best Quality (1080p+)
  - High Quality (1080p)
  - Medium Quality (720p)
  - Low Quality (480p)

- **Audio Extraction**:
  - MP3 (320kbps)
  - M4A (256kbps)
  - Opus (192kbps)

### Custom Formats Tab

For power users who want full control:

**Format Organization:**
1. **Video + Audio (Ready to Play)**: Combined formats up to 480p
   - Instant playback, no merging needed
   - Perfect for quick downloads

2. **Audio Only Formats**: Extract audio only
   - Bitrate comparison
   - Codec information (Opus, AAC, MP3)
   - Sample rate details
   - Perfect for music and podcasts

3. **Video Only (No Audio)**: High-quality video streams
   - 1080p, 1440p, 4K, and higher resolutions
   - **Automatically merges with best audio** using FFmpeg
   - Clear indication of "No Audio" status
   - Resolution and FPS information
   - Codec details (VP9, H264, AV1)
   - File size estimates

### Advanced Settings Tab

Fine-tune your downloads:

**Download Settings**
- Custom save location
- Filename templates
- Concurrent download limits
- Retry attempts
- Connection timeout

**Post-Processing**
- Embed thumbnails
- Embed metadata
- Auto-convert to MP4
- Extract audio copy

**Subtitle Settings**
- Auto-download subtitles
- Multiple language selection
- Format options (SRT, VTT, ASS)
- Embed or separate files

### Batch Download Tab

Download multiple videos efficiently:

- Paste multiple URLs (one per line)
- Playlist support (YouTube, Vimeo)
- Channel downloads
- Quality presets for all videos

---

## ⚙️ Configuration

### Default Settings

Settings are automatically saved in:
- **Windows**: `C:\Users\<username>\.converso\settings.json`
- **macOS/Linux**: `~/.converso/settings.json`

### Customizable Options

```json
{
  "download_location": "C:\\Users\\<username>\\Downloads\\Converso",
  "quality_preference": "best",
  "output_format": "mp4",
  "concurrent_downloads": 3,
  "embed_thumbnail": true,
  "embed_metadata": true,
  "filename_template": "{title}_{resolution}",
  "audio_bitrate": "192k",
  "retry_attempts": 3
}
```

### Filename Templates

Use these variables in your filename template:

- `{title}`: Video title
- `{uploader}`: Channel/uploader name
- `{date}`: Upload date
- `{resolution}`: Video resolution (e.g., 1080p)
- `{id}`: Video ID

Example: `{uploader} - {title} [{resolution}]`

---

## 🎨 Platform Support

### YouTube Only
This version is **optimized exclusively for YouTube** with advanced features:

- **Full YouTube Support**: All video types and quality levels
- **Search Integration**: Built-in YouTube search
- **Playlists & Channels**: Download entire playlists or channel videos
- **Live Streams**: Download live streams and premieres
- **All Quality Levels**: From 144p to 8K resolution
- **Member-Only Content**: If you have access
- **Age-Restricted Videos**: With appropriate authentication

**Why YouTube Only?**
- Focused optimization for best performance
- Integrated search functionality
- Better quality detection
- Faster processing
- More reliable downloads

---

## 🐛 Troubleshooting

### Common Issues

**Issue**: "FFmpeg not found"
- **Solution**: Ensure FFmpeg is installed and added to PATH
- **Verify**: Run `ffmpeg -version` in terminal

**Issue**: "Unable to download video"
- **Solution**: Update yt-dlp to latest version
- **Command**: `pip install --upgrade yt-dlp`

**Issue**: "Video format not available"
- **Solution**: Try a different quality preset or use custom formats

**Issue**: "Slow download speed"
- **Solution**: 
  - Check your internet connection
  - Reduce concurrent downloads
  - Try different time of day

### Getting Help

1. Check the [yt-dlp documentation](https://github.com/yt-dlp/yt-dlp)
2. Verify FFmpeg installation
3. Update all dependencies
4. Check platform-specific limitations

---

## 📝 Best Practices

### For Best Results

1. **Keep Software Updated**
   ```bash
   pip install --upgrade yt-dlp streamlit
   ```

2. **Use Appropriate Quality**
   - Higher quality = larger files
   - Consider your storage space
   - Choose format based on use case

3. **Respect Copyright**
   - Only download content you have rights to
   - Follow platform terms of service
   - Use for personal purposes only

4. **Optimize Settings**
   - Set reasonable concurrent download limits
   - Use filename templates for organization
   - Enable metadata embedding for media libraries

---

## 🔒 Privacy & Security

- **No Data Collection**: All processing happens locally
- **No Account Required**: No sign-up or registration
- **Offline Capable**: Works without internet (for downloaded videos)
- **Open Source**: Transparent codebase

---

## 📜 License

**For Personal Use Only**

This software is provided for personal, non-commercial use. Users must:
- Respect copyright laws and intellectual property rights
- Follow platform terms of service
- Not use for commercial purposes without proper authorization
- Not distribute copyrighted content

---

## 🙏 Acknowledgments

Built with amazing open-source technologies:

- [yt-dlp](https://github.com/yt-dlp/yt-dlp) - Universal video downloader
- [FFmpeg](https://ffmpeg.org/) - Multimedia framework
- [Streamlit](https://streamlit.io/) - Web app framework
- [Inter Font](https://rsms.me/inter/) - UI typeface

---

## 📞 Support

For issues and questions:

1. Check this README for common solutions
2. Review [yt-dlp documentation](https://github.com/yt-dlp/yt-dlp)
3. Ensure all dependencies are up to date

---

## 🎯 Roadmap

Future enhancements planned:

- [ ] Download queue management
- [ ] Download history with search
- [ ] Playlist batch processing improvements
- [ ] Network optimization tools
- [ ] Automatic subtitle generation
- [ ] Video preview before download
- [ ] Resume interrupted downloads
- [ ] Schedule downloads
- [ ] Cloud storage integration

---

## ⚡ Quick Tips

💡 **Tip**: Use keyboard shortcuts - Press Enter after pasting URL to quickly fetch info

💡 **Tip**: Hover over format options to see detailed codec information

💡 **Tip**: Enable "Embed Thumbnail" for better media library organization

💡 **Tip**: Use filename templates to automatically organize downloads

💡 **Tip**: Check "Available Formats" tab for best quality/size ratio

---

---

## 🏁 License

**Converso Empire License (CEL)**

All Converso Empire projects are protected under the Converso Empire License (CEL).

**Terms:**
- ✅ Free for personal use
- ✅ Modify for personal use
- ❌ Commercial use prohibited
- ❌ Redistribution prohibited
- ❌ Unauthorized reproduction strictly prohibited

**© 2025 Converso Empire. All rights reserved.**

For licensing inquiries, contact: [Converso Empire](https://github.com/Converso-Empire)

---

## 🙏 Acknowledgments

Built with amazing open-source technologies:
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) - Universal video downloader
- [FFmpeg](https://ffmpeg.org/) - Multimedia framework
- [Streamlit](https://streamlit.io/) - Web app framework

---

## 📞 Support

- 🐛 [Report Bug](https://github.com/Converso-Empire/converso-downloader/issues)
- 💡 [Request Feature](https://github.com/Converso-Empire/converso-downloader/issues)
- 📖 [Documentation](https://github.com/Converso-Empire/converso-downloader)

---

<div align="center">

### 🌟 Made with ❤️ by [Converso Empire](https://github.com/Converso-Empire)

**Converso Downloader v2.1.3** • Production Ready

*Empowering users with professional tools*

[⬇️ Download Now](https://github.com/Converso-Empire/converso-downloader/releases/latest) • [⭐ Star on GitHub](https://github.com/Converso-Empire/converso-downloader)

© 2025 Converso Empire • All Rights Reserved

</div>
