"""
Production Build Test Script
Run this before releasing to verify everything works
"""

import os
import sys
from pathlib import Path

def test_files_exist():
    """Check if all required files exist"""
    print("=" * 60)
    print("Testing File Structure")
    print("=" * 60)
    
    required_files = [
        'launcher.py',
        'app.py',
        'version.py',
        'ui_components.py',
        'streamlit_config.toml',
        'converso-downloader.spec',
        'requirements.txt',
        'CHANGELOG.md',
        'PRODUCTION_READY.md',
        'HOW_TO_RUN.txt',
        'config/__init__.py',
        'utils/__init__.py',
        'utils/update_checker.py',
    ]
    
    missing = []
    for file in required_files:
        path = Path(file)
        if path.exists():
            print(f"✅ {file}")
        else:
            print(f"❌ {file} - MISSING!")
            missing.append(file)
    
    if missing:
        print(f"\n⚠️  Missing {len(missing)} files!")
        return False
    else:
        print("\n✅ All files present!")
        return True

def test_version():
    """Check version information"""
    print("\n" + "=" * 60)
    print("Testing Version")
    print("=" * 60)
    
    try:
        from version import __version__, __app_name__, __repo__
        print(f"✅ App Name: {__app_name__}")
        print(f"✅ Version: {__version__}")
        print(f"✅ Repository: {__repo__}")
        
        if __version__ != "2.1.4":
            print(f"⚠️  Warning: Expected version 2.1.4, got {__version__}")
            return False
        return True
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_imports():
    """Test if all imports work"""
    print("\n" + "=" * 60)
    print("Testing Imports")
    print("=" * 60)
    
    imports = [
        ('streamlit', 'Streamlit'),
        ('yt_dlp', 'yt-dlp'),
        ('PIL', 'Pillow'),
        ('requests', 'Requests'),
        ('packaging', 'Packaging'),
    ]
    
    failed = []
    for module, name in imports:
        try:
            __import__(module)
            print(f"✅ {name}")
        except ImportError as e:
            print(f"❌ {name} - NOT INSTALLED!")
            failed.append(name)
    
    if failed:
        print(f"\n⚠️  Missing {len(failed)} packages. Run: pip install -r requirements.txt")
        return False
    else:
        print("\n✅ All dependencies installed!")
        return True

def test_config():
    """Test Streamlit configuration"""
    print("\n" + "=" * 60)
    print("Testing Streamlit Config")
    print("=" * 60)
    
    config_path = Path('streamlit_config.toml')
    if not config_path.exists():
        print("❌ streamlit_config.toml not found!")
        return False
    
    with open(config_path, 'r') as f:
        content = f.read()
        
    checks = [
        ('developmentMode = false', 'Development mode disabled'),
        ('enableCORS = false', 'CORS disabled'),
        ('headless = true', 'Headless mode enabled'),
        ('gatherUsageStats = false', 'Stats collection disabled'),
    ]
    
    all_pass = True
    for check, desc in checks:
        if check in content:
            print(f"✅ {desc}")
        else:
            print(f"❌ {desc} - NOT CONFIGURED!")
            all_pass = False
    
    return all_pass

def test_spec_file():
    """Test PyInstaller spec file"""
    print("\n" + "=" * 60)
    print("Testing PyInstaller Spec")
    print("=" * 60)
    
    spec_path = Path('converso-downloader.spec')
    if not spec_path.exists():
        print("❌ converso-downloader.spec not found!")
        return False
    
    with open(spec_path, 'r') as f:
        content = f.read()
    
    checks = [
        ("['launcher.py']", 'Entry point is launcher.py'),
        ('safe_copy_metadata', 'Safe metadata collection'),
        ('streamlit_config.toml', 'Config file included'),
        ('console=False', 'Console disabled'),
        ("('app.py', '.')", 'App file included'),
    ]
    
    all_pass = True
    for check, desc in checks:
        if check in content:
            print(f"✅ {desc}")
        else:
            print(f"❌ {desc} - NOT CONFIGURED!")
            all_pass = False
    
    return all_pass

def test_update_checker():
    """Test update checker functionality"""
    print("\n" + "=" * 60)
    print("Testing Update Checker")
    print("=" * 60)
    
    try:
        from utils.update_checker import UpdateChecker
        from version import __version__, __repo__
        
        checker = UpdateChecker(__version__, __repo__)
        print(f"✅ Update checker initialized")
        print(f"✅ Current version: {__version__}")
        print(f"✅ Repository: {__repo__}")
        print(f"✅ API URL: {checker.api_url}")
        
        return True
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def main():
    """Run all tests"""
    print("\n")
    print("╔" + "=" * 58 + "╗")
    print("║" + " " * 10 + "PRODUCTION BUILD TEST SUITE" + " " * 20 + "║")
    print("║" + " " * 15 + "Converso Downloader v2.1.4" + " " * 15 + "║")
    print("╚" + "=" * 58 + "╝")
    
    tests = [
        ("File Structure", test_files_exist),
        ("Version Info", test_version),
        ("Dependencies", test_imports),
        ("Streamlit Config", test_config),
        ("PyInstaller Spec", test_spec_file),
        ("Update Checker", test_update_checker),
    ]
    
    results = []
    for name, test_func in tests:
        try:
            result = test_func()
            results.append((name, result))
        except Exception as e:
            print(f"\n❌ {name} test failed with exception: {e}")
            results.append((name, False))
    
    # Summary
    print("\n" + "=" * 60)
    print("TEST SUMMARY")
    print("=" * 60)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status} - {name}")
    
    print("\n" + "=" * 60)
    print(f"Results: {passed}/{total} tests passed")
    print("=" * 60)
    
    if passed == total:
        print("\n🎉 ALL TESTS PASSED!")
        print("✅ BUILD IS READY FOR PRODUCTION")
        print("\nNext steps:")
        print("1. Run: pyinstaller converso-downloader.spec")
        print("2. Test: .\\dist\\ConversoDownloader.exe")
        print("3. Release: git tag -a v2.1.4 -m 'Release v2.1.4'")
        return 0
    else:
        print(f"\n⚠️  {total - passed} TEST(S) FAILED")
        print("❌ FIX ISSUES BEFORE RELEASING")
        return 1

if __name__ == "__main__":
    sys.exit(main())
