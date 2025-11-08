# 💬 Support

Need help with **Converso Downloader**? We're here to assist you!

---

## 🚀 Quick Links

- 📖 [Full Documentation](../README.md)
- ❓ [FAQ](#-frequently-asked-questions)
- 🐛 [Report a Bug](https://github.com/Converso-Empire/converso-downloader/issues/new?template=bug_report.yml)
- 💡 [Request a Feature](https://github.com/Converso-Empire/converso-downloader/issues/new?template=feature_request.yml)
- ❓ [Ask a Question](https://github.com/Converso-Empire/converso-downloader/issues/new?template=question.yml)

---

## 📚 Getting Help

### 1. Check the Documentation

Before asking for help, please review:

- **[README.md](../README.md)** - Complete user guide
- **[Installation Guide](../README.md#-quick-start)** - Setup instructions
- **[Usage Guide](../README.md#-how-to-use)** - How to use the app
- **[Troubleshooting](../README.md#-troubleshooting)** - Common issues

### 2. Search Existing Issues

Someone may have already asked your question:

- [Search Issues](https://github.com/Converso-Empire/converso-downloader/issues)
- [Search Discussions](https://github.com/Converso-Empire/converso-downloader/discussions)

### 3. Ask the Community

- 💬 [Start a Discussion](https://github.com/Converso-Empire/converso-downloader/discussions)
- ❓ [Open a Question Issue](https://github.com/Converso-Empire/converso-downloader/issues/new?template=question.yml)

---

## ❓ Frequently Asked Questions

### Installation & Setup

<details>
<summary><strong>Q: Where do I download Converso Downloader?</strong></summary>

**A:** Download the latest version from our official GitHub Releases page:
- [Latest Release](https://github.com/Converso-Empire/converso-downloader/releases/latest)

Choose the package for your platform:
- Windows: `Converso-Downloader-Windows.zip`
- macOS: `Converso-Downloader-macOS.tar.gz`
- Linux: `Converso-Downloader-Linux.tar.gz`
</details>

<details>
<summary><strong>Q: Do I need to install Python?</strong></summary>

**A:** No! If you download the pre-built executable from releases, Python is already bundled. You can just extract and run.

If you want to run from source, you'll need Python 3.8 or higher.
</details>

<details>
<summary><strong>Q: Do I need to install FFmpeg separately?</strong></summary>

**A:** No! FFmpeg is included in all release packages. Just extract and run!

If running from source, you'll need to install FFmpeg separately.
</details>

<details>
<summary><strong>Q: How do I run the application?</strong></summary>

**A:** 
- **Windows:** Double-click `ConversoDownloader.exe`
- **macOS/Linux:** Run `./ConversoDownloader` in terminal
- **From Source:** Run `streamlit run app.py`

The app will open automatically in your default browser.
</details>

### Usage

<details>
<summary><strong>Q: How do I download a video?</strong></summary>

**A:** Three ways to find videos:
1. **Search by name:** Type the video name in the search box
2. **Paste URL:** Paste any YouTube URL
3. **Enter ID:** Just the 11-character video ID

Then choose quality and click download!
</details>

<details>
<summary><strong>Q: Where are my downloads saved?</strong></summary>

**A:** By default:
- Windows: `C:\Users\<username>\Downloads\Converso`
- macOS/Linux: `~/Downloads/Converso`

You can change this in **Advanced Settings** → **Download Location**
</details>

<details>
<summary><strong>Q: What video qualities are available?</strong></summary>

**A:** Converso Downloader supports all YouTube qualities:
- 8K (4320p)
- 4K (2160p)
- 1440p (2K)
- 1080p (Full HD)
- 720p (HD)
- 480p
- 360p
- 144p

The app automatically merges video and audio for the best quality.
</details>

<details>
<summary><strong>Q: Can I download only audio?</strong></summary>

**A:** Yes! Go to **Quick Download** → **Audio** tab and choose:
- MP3 (320kbps)
- M4A (256kbps)
- Opus (192kbps)
</details>

<details>
<summary><strong>Q: Can I download playlists?</strong></summary>

**A:** Yes! Go to the **Batch Download** tab and paste playlist URLs.
</details>

### Troubleshooting

<details>
<summary><strong>Q: The app won't start</strong></summary>

**A:** Try these steps:
1. Make sure you extracted the full archive
2. Check antivirus isn't blocking it
3. On macOS: Right-click → Open (if security warning appears)
4. On Linux: Make sure file is executable (`chmod +x ConversoDownloader`)
5. Check if another instance is already running
</details>

<details>
<summary><strong>Q: "FFmpeg not found" error</strong></summary>

**A:** 
- **Pre-built executable:** FFmpeg is included! Make sure you extracted the `ffmpeg/` folder
- **Running from source:** Install FFmpeg separately:
  - Windows: Download from ffmpeg.org
  - macOS: `brew install ffmpeg`
  - Linux: `sudo apt install ffmpeg`
</details>

<details>
<summary><strong>Q: Download fails or is very slow</strong></summary>

**A:** 
1. Check your internet connection
2. Try a different video quality
3. Check if YouTube is accessible in your region
4. Update to the latest version of Converso Downloader
5. Some videos may have download restrictions
</details>

<details>
<summary><strong>Q: Antivirus flags the executable as malware</strong></summary>

**A:** This is a false positive (common with PyInstaller executables):
1. Download only from official GitHub Releases
2. Verify the file size matches expected size
3. Add exception to your antivirus
4. The source code is open - you can build it yourself!
</details>

<details>
<summary><strong>Q: Video and audio are out of sync</strong></summary>

**A:** This is rare but can happen:
1. Make sure FFmpeg is working correctly
2. Try re-downloading the video
3. Report the issue with the video URL
</details>

<details>
<summary><strong>Q: Can't find a specific video</strong></summary>

**A:** 
1. Try pasting the URL directly instead of searching
2. Make sure the video is public (not private/unlisted)
3. Check if the video is available in your region
4. Some age-restricted videos may require authentication
</details>

### Features

<details>
<summary><strong>Q: Can I download from other platforms besides YouTube?</strong></summary>

**A:** Currently, Converso Downloader is optimized exclusively for YouTube. This allows us to provide the best YouTube experience with features like integrated search.
</details>

<details>
<summary><strong>Q: Can I schedule downloads?</strong></summary>

**A:** Not yet, but it's on our roadmap! Check the [README](../README.md#-roadmap) for planned features.
</details>

<details>
<summary><strong>Q: Does it support subtitles?</strong></summary>

**A:** Yes! Go to **Advanced Settings** → **Subtitle Settings** to configure subtitle downloads.
</details>

<details>
<summary><strong>Q: Can I convert video formats?</strong></summary>

**A:** Yes! The app supports conversion to MP4, MKV, and WebM. Configure in **Advanced Settings**.
</details>

### Legal & Privacy

<details>
<summary><strong>Q: Is it legal to use Converso Downloader?</strong></summary>

**A:** Converso Downloader is a tool. The legality depends on how you use it:
- ✅ Downloading your own content
- ✅ Downloading content you have rights to
- ✅ Downloading Creative Commons content
- ❌ Downloading copyrighted content without permission
- ❌ Commercial use without proper licensing

Always respect copyright laws and YouTube's Terms of Service.
</details>

<details>
<summary><strong>Q: Does Converso Downloader collect my data?</strong></summary>

**A:** **No!** We do NOT collect any data:
- ❌ No analytics or tracking
- ❌ No telemetry
- ❌ No account required
- ❌ No data sent to external servers
- ✅ All processing happens locally on your machine
</details>

<details>
<summary><strong>Q: What is the license?</strong></summary>

**A:** Converso Downloader is licensed under the **Converso Empire License (CEL)**:
- ✅ Free for personal use
- ✅ Can modify for personal use
- ❌ Commercial use prohibited
- ❌ Redistribution prohibited

See [LICENSE](../LICENSE) for full details.
</details>

### Technical

<details>
<summary><strong>Q: What are the system requirements?</strong></summary>

**A:** 
- **Pre-built executable:** Windows 10+, macOS 10.13+, or modern Linux
- **From source:** Python 3.8+ and FFmpeg
- **RAM:** 2GB minimum, 4GB recommended
- **Storage:** 100MB for app + space for downloads
- **Internet:** Required for downloads
</details>

<details>
<summary><strong>Q: Can I run it offline?</strong></summary>

**A:** The app launches offline, but you need internet to:
- Search for videos
- Download videos
- Fetch video information
</details>

<details>
<summary><strong>Q: How do I update to a new version?</strong></summary>

**A:** 
1. Download the latest release
2. Extract to a new folder (or replace old files)
3. Run the new version
4. Your settings are preserved!
</details>

---

## 🐛 Found a Bug?

If you've found a bug, please:

1. Check if it's already reported in [Issues](https://github.com/Converso-Empire/converso-downloader/issues)
2. If not, [create a new bug report](https://github.com/Converso-Empire/converso-downloader/issues/new?template=bug_report.yml)
3. Include as much detail as possible

---

## 💡 Have a Feature Idea?

We love feature suggestions!

1. Check [existing feature requests](https://github.com/Converso-Empire/converso-downloader/issues?q=is%3Aissue+label%3Aenhancement)
2. If it's new, [submit a feature request](https://github.com/Converso-Empire/converso-downloader/issues/new?template=feature_request.yml)
3. Describe the use case clearly

---

## 🤝 Want to Contribute?

Contributions are welcome! See:

- [Contributing Guide](CONTRIBUTING.md)
- [Code of Conduct](CODE_OF_CONDUCT.md)

---

## 📞 Still Need Help?

If you can't find what you need:

1. **Open a Question Issue:**
   - [Ask a Question](https://github.com/Converso-Empire/converso-downloader/issues/new?template=question.yml)

2. **Start a Discussion:**
   - [Community Discussions](https://github.com/Converso-Empire/converso-downloader/discussions)

3. **Check GitHub Issues:**
   - Someone may have already asked your question

---

## ⏱️ Response Time

- **Questions:** Typically answered within 24-48 hours
- **Bug Reports:** Reviewed within 2-3 days
- **Feature Requests:** Evaluated regularly

Please be patient! This project is maintained by volunteers.

---

## 🌟 Community

Join our community:

- ⭐ [Star the project](https://github.com/Converso-Empire/converso-downloader)
- 💬 [Discussions](https://github.com/Converso-Empire/converso-downloader/discussions)
- 🐛 [Issues](https://github.com/Converso-Empire/converso-downloader/issues)

---

## 📚 Additional Resources

- [yt-dlp Documentation](https://github.com/yt-dlp/yt-dlp)
- [FFmpeg Documentation](https://ffmpeg.org/documentation.html)
- [Streamlit Documentation](https://docs.streamlit.io/)

---

<div align="center">

## 🙏 Thank You!

Thank you for using **Converso Downloader**!

**Created by [Converso Empire](https://github.com/Converso-Empire)**

*Empowering users with professional tools*

© 2025 Converso Empire. All rights reserved.

</div>
