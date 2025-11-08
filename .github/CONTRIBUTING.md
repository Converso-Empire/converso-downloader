# 🤝 Contributing to Converso Downloader

First off, thank you for considering contributing to Converso Downloader! 🎉

This document provides guidelines for contributing to this project. Following these guidelines helps maintain code quality and makes the review process smoother for everyone.

---

## 📋 Table of Contents

- [Code of Conduct](#-code-of-conduct)
- [How Can I Contribute?](#-how-can-i-contribute)
- [Development Setup](#-development-setup)
- [Coding Standards](#-coding-standards)
- [Commit Guidelines](#-commit-guidelines)
- [Pull Request Process](#-pull-request-process)
- [Issue Guidelines](#-issue-guidelines)
- [License](#-license)

---

## 📜 Code of Conduct

This project adheres to a Code of Conduct that all contributors are expected to follow. By participating, you are expected to uphold this code. Please report unacceptable behavior to the project maintainers.

**Key Points:**
- Be respectful and inclusive
- Accept constructive criticism gracefully
- Focus on what is best for the community
- Show empathy towards other contributors

---

## 🎯 How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check existing issues. When creating a bug report, include as many details as possible:

- Use the bug report template
- Provide system information (OS, version, etc.)
- Include error messages and logs
- Describe steps to reproduce
- Include screenshots if applicable

### Suggesting Features

Feature suggestions are welcome! Please:

- Use the feature request template
- Explain the use case clearly
- Describe why this feature would be useful
- Consider if it aligns with project goals

### Code Contributions

We welcome code contributions! Here's how:

1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/amazing-feature`)
3. **Make your changes**
4. **Test thoroughly**
5. **Commit your changes** (see commit guidelines)
6. **Push to your fork** (`git push origin feature/amazing-feature`)
7. **Open a Pull Request**

### Documentation

Help improve documentation by:

- Fixing typos and errors
- Adding examples and clarifications
- Improving README sections
- Writing tutorials or guides

---

## 🛠️ Development Setup

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- FFmpeg (for testing download functionality)
- Git

### Setup Steps

```bash
# 1. Fork and clone the repository
git clone https://github.com/YOUR_USERNAME/converso-downloader.git
cd converso-downloader

# 2. Create a virtual environment (recommended)
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Install development dependencies (if applicable)
pip install pytest black flake8 mypy

# 5. Run the application
streamlit run app.py
```

### Project Structure

```
converso-downloader/
├── app.py                  # Main application entry point
├── ui_components.py        # UI components and layouts
├── version.py              # Version information
├── config/                 # Configuration management
│   └── settings.py
├── utils/                  # Utility modules
│   ├── downloader.py       # Download engine
│   ├── file_utils.py       # File operations
│   ├── format_handler.py   # Format processing
│   ├── validators.py       # Input validation
│   └── youtube_search.py   # Search functionality
└── .github/                # GitHub templates and workflows
    ├── workflows/          # CI/CD workflows
    └── ISSUE_TEMPLATE/     # Issue templates
```

---

## 💻 Coding Standards

### Python Style Guide

We follow PEP 8 with some modifications:

- **Line Length**: Maximum 100 characters
- **Indentation**: 4 spaces (no tabs)
- **Quotes**: Double quotes for strings
- **Imports**: Grouped and sorted (stdlib, third-party, local)

### Code Quality Tools

```bash
# Format code with Black
black .

# Check code style with Flake8
flake8 .

# Type checking with MyPy
mypy .
```

### Best Practices

**1. Write Clean Code**
- Use descriptive variable names
- Keep functions small and focused
- Add comments for complex logic
- Follow DRY (Don't Repeat Yourself)

**2. Error Handling**
```python
# Good
try:
    result = download_video(url)
except DownloadError as e:
    logger.error(f"Download failed: {e}")
    st.error("Failed to download video. Please try again.")

# Avoid bare excepts
try:
    result = download_video(url)
except:  # Bad - too broad
    pass
```

**3. Documentation**
```python
def download_video(url: str, quality: str = "best") -> bool:
    """
    Download a YouTube video.
    
    Args:
        url: YouTube video URL
        quality: Video quality preset (best, high, medium, low)
        
    Returns:
        True if download successful, False otherwise
        
    Raises:
        ValueError: If URL is invalid
        DownloadError: If download fails
    """
    pass
```

**4. Type Hints**
```python
from typing import Dict, List, Optional

def process_formats(formats: List[Dict]) -> Optional[str]:
    """Process video formats and return best format ID."""
    pass
```

---

## 📝 Commit Guidelines

### Commit Message Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Types

- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring
- `perf`: Performance improvements
- `test`: Adding or updating tests
- `chore`: Maintenance tasks
- `ci`: CI/CD changes

### Examples

```bash
# Good commit messages
feat(search): add real-time search results
fix(download): resolve FFmpeg path issue on Windows
docs(readme): update installation instructions
refactor(ui): simplify video info card rendering

# Bad commit messages
fixed bug
update
changes
WIP
```

### Commit Best Practices

- **Atomic commits**: One logical change per commit
- **Present tense**: "Add feature" not "Added feature"
- **Imperative mood**: "Fix bug" not "Fixes bug"
- **Reference issues**: "Fixes #123" or "Closes #456"

---

## 🔀 Pull Request Process

### Before Submitting

1. **Update your branch**
   ```bash
   git checkout main
   git pull upstream main
   git checkout your-branch
   git rebase main
   ```

2. **Test your changes**
   - Run the application
   - Test on multiple platforms (if possible)
   - Verify no new warnings or errors

3. **Update documentation**
   - Update README if needed
   - Add/update docstrings
   - Include code comments

4. **Check code quality**
   ```bash
   black .
   flake8 .
   ```

### PR Checklist

- [ ] Code follows project style guidelines
- [ ] Self-review completed
- [ ] Comments added for complex code
- [ ] Documentation updated
- [ ] No new warnings generated
- [ ] Tested thoroughly
- [ ] Commit messages follow guidelines

### PR Description

- Use the pull request template
- Describe what changes were made
- Explain why changes were necessary
- Reference related issues
- Include screenshots for UI changes

### Review Process

1. **Automated checks** run on your PR
2. **Maintainer review** (may request changes)
3. **Address feedback** if requested
4. **Approval** from maintainer
5. **Merge** into main branch

---

## 🐛 Issue Guidelines

### Before Creating an Issue

- **Search** for existing issues
- **Check** documentation and README
- **Verify** you're using the latest version
- **Test** on a clean environment if possible

### Issue Types

**Bug Reports**
- Use bug report template
- Include reproduction steps
- Provide system information
- Add error logs/screenshots

**Feature Requests**
- Use feature request template
- Explain use cases clearly
- Describe expected behavior
- Consider implementation complexity

**Questions**
- Use question template
- Be specific and clear
- Include what you've tried
- Provide context

---

## 🧪 Testing

### Manual Testing

Test your changes by:

1. **Running from source**
   ```bash
   streamlit run app.py
   ```

2. **Testing core features**
   - Search functionality
   - Video download
   - Audio extraction
   - Format selection
   - Settings persistence

3. **Testing edge cases**
   - Invalid URLs
   - Network errors
   - Large files
   - Multiple concurrent downloads

### Platform Testing

If possible, test on:
- ✅ Windows 10/11
- ✅ macOS (Intel/Apple Silicon)
- ✅ Linux (Ubuntu/Debian/Fedora)

---

## 📦 Building Executables

To test executable builds:

```bash
# Install PyInstaller
pip install pyinstaller

# Build executable
pyinstaller converso-downloader.spec

# Test the executable
cd dist
./ConversoDownloader  # or ConversoDownloader.exe on Windows
```

---

## 🎨 UI/UX Guidelines

When modifying the UI:

- **Consistency**: Match existing design patterns
- **Accessibility**: Use clear labels and colors
- **Responsiveness**: Test on different screen sizes
- **Feedback**: Provide user feedback for actions
- **Error Messages**: Make them clear and actionable

### Streamlit Best Practices

```python
# Use session state for persistence
if 'video_info' not in st.session_state:
    st.session_state.video_info = None

# Provide user feedback
with st.spinner("Downloading..."):
    result = download_video(url)
    
if result:
    st.success("Download completed!")
else:
    st.error("Download failed. Please try again.")
```

---

## 📚 Resources

### Documentation

- [Python PEP 8](https://pep8.org/)
- [Streamlit Docs](https://docs.streamlit.io/)
- [yt-dlp Documentation](https://github.com/yt-dlp/yt-dlp)
- [FFmpeg Documentation](https://ffmpeg.org/documentation.html)

### Tools

- [Black](https://black.readthedocs.io/) - Code formatter
- [Flake8](https://flake8.pycqa.org/) - Style checker
- [MyPy](http://mypy-lang.org/) - Type checker
- [PyInstaller](https://pyinstaller.org/) - Executable builder

---

## 🏁 License

By contributing to Converso Downloader, you agree that your contributions will be licensed under the Converso Empire License (CEL).

**Key Points:**
- Personal use is allowed
- Commercial use is prohibited
- Redistribution is prohibited
- All rights reserved by Converso Empire

See [LICENSE](../LICENSE) for full details.

---

## 💬 Questions?

If you have questions about contributing:

- 📖 Check the [README](../README.md)
- 💬 Start a [Discussion](https://github.com/Converso-Empire/converso-downloader/discussions)
- ❓ Open a [Question Issue](https://github.com/Converso-Empire/converso-downloader/issues/new?template=question.yml)

---

## 🙏 Thank You!

Your contributions make Converso Downloader better for everyone. We appreciate your time and effort!

**Happy Contributing! 🎉**

---

<div align="center">

**Created by [Converso Empire](https://github.com/Converso-Empire)**

*Empowering the community with professional tools*

© 2025 Converso Empire. All rights reserved.

</div>
