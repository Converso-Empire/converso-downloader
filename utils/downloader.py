"""Video downloader using yt-dlp for Converso Pro Downloader"""

import yt_dlp
import os
from typing import Dict, Optional, Callable
from pathlib import Path
import time


class VideoInfoExtractor:
    """Handles video information extraction"""
    
    def __init__(self):
        self.cache = {}
        self.ydl_opts = {
            'quiet': True,
            'no_warnings': True,
            'extract_flat': False,
            'skip_download': True,
        }
    
    def validate_url(self, url: str) -> tuple[bool, str]:
        """
        Validate URL and return (is_valid, error_message)
        """
        from .validators import URLValidator
        return URLValidator.is_valid_url(url)
    
    def extract_info(self, url: str, use_cache: bool = True) -> Optional[Dict]:
        """
        Extract comprehensive video information
        Returns dict with video metadata and formats
        """
        # Check cache
        if use_cache and url in self.cache:
            return self.cache[url]
        
        try:
            with yt_dlp.YoutubeDL(self.ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                
                if not info:
                    return None
                
                # Process and structure the information
                processed_info = {
                    'id': info.get('id', ''),
                    'title': info.get('title', 'Unknown Title'),
                    'uploader': info.get('uploader', 'Unknown'),
                    'duration': info.get('duration', 0),
                    'duration_formatted': self._format_duration(info.get('duration', 0)),
                    'view_count': info.get('view_count', 0),
                    'like_count': info.get('like_count'),
                    'upload_date': self._format_date(info.get('upload_date')),
                    'description': info.get('description', ''),
                    'thumbnail': self.get_best_thumbnail(info.get('thumbnails', [])),
                    'formats': info.get('formats', []),
                    'subtitles': info.get('subtitles', {}),
                    'automatic_captions': info.get('automatic_captions', {}),
                    'categories': info.get('categories', []),
                    'tags': info.get('tags', []),
                    'resolution': self._get_max_resolution(info.get('formats', [])),
                    'estimated_size': self._estimate_total_size(info.get('formats', [])),
                    'webpage_url': info.get('webpage_url', url),
                }
                
                # Cache the result
                self.cache[url] = processed_info
                
                return processed_info
                
        except Exception as e:
            print(f"Error extracting info: {e}")
            return None
    
    def get_best_thumbnail(self, thumbnails: list) -> str:
        """Select highest quality thumbnail"""
        if not thumbnails:
            return ""
        
        # Filter out any None or invalid entries
        valid_thumbs = [t for t in thumbnails if t and isinstance(t, dict) and t.get('url')]
        
        if not valid_thumbs:
            return ""
        
        # Sort by resolution (width * height)
        sorted_thumbs = sorted(
            valid_thumbs,
            key=lambda x: (x.get('width', 0) * x.get('height', 0)),
            reverse=True
        )
        
        return sorted_thumbs[0].get('url', '') if sorted_thumbs else ""
    
    def estimate_size(self, format_dict: dict) -> int:
        """Estimate download size in bytes"""
        return format_dict.get('filesize') or format_dict.get('filesize_approx', 0)
    
    def _format_duration(self, seconds: Optional[int]) -> str:
        """Format duration to readable string"""
        if not seconds:
            return "Unknown"
        
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        secs = seconds % 60
        
        if hours > 0:
            return f"{hours}:{minutes:02d}:{secs:02d}"
        return f"{minutes}:{secs:02d}"
    
    def _format_date(self, date_str: Optional[str]) -> str:
        """Format upload date"""
        if not date_str:
            return "Unknown"
        
        try:
            # Date is in format YYYYMMDD
            from datetime import datetime
            date_obj = datetime.strptime(date_str, '%Y%m%d')
            return date_obj.strftime('%B %d, %Y')
        except Exception:
            return date_str
    
    def _get_max_resolution(self, formats: list) -> str:
        """Get maximum available resolution"""
        max_height = 0
        for fmt in formats:
            if height := fmt.get('height'):
                max_height = max(max_height, height)
        
        return f"{max_height}p" if max_height > 0 else "Unknown"
    
    def _estimate_total_size(self, formats: list) -> str:
        """Estimate size of best quality download"""
        from .file_utils import FileManager
        
        max_size = 0
        for fmt in formats:
            if size := (fmt.get('filesize') or fmt.get('filesize_approx', 0)):
                max_size = max(max_size, size)
        
        return FileManager.format_size(max_size)


class VideoDownloader:
    """Handles video downloading with progress tracking"""
    
    def __init__(self, output_path: str, progress_callback: Optional[Callable] = None):
        self.output_path = Path(output_path)
        self.output_path.mkdir(parents=True, exist_ok=True)
        self.progress_callback = progress_callback
        self.is_cancelled = False
    
    def download(self, url: str, format_id: str = 'best', options: Optional[Dict] = None) -> Dict:
        """
        Download video with specified format
        Returns: dict with download status and file path
        """
        options = options or {}
        
        # Build yt-dlp options
        ydl_opts = {
            'format': format_id,
            'outtmpl': str(self.output_path / '%(title)s.%(ext)s'),
            'progress_hooks': [self._progress_hook],
            'quiet': False,
            'no_warnings': False,
            # Use most compatible format for merging (H.264 + AAC in MP4)
            'merge_output_format': 'mp4',
            'postprocessor_args': {
                'ffmpeg': [
                    '-c:v', 'libx264',  # H.264 video codec (most compatible)
                    '-c:a', 'aac',      # AAC audio codec (most compatible)
                    '-preset', 'fast',  # Fast encoding
                    '-movflags', '+faststart',  # Web optimization
                ]
            },
        }
        
        # Override merge format if specifically requested
        if options.get('merge_output_format'):
            ydl_opts['merge_output_format'] = options['merge_output_format']
        
        # Add merge options for video+audio
        if options.get('merge_with'):
            ydl_opts['format'] = f"{format_id}+{options['merge_with']}"
        
        # Audio extraction options
        if options.get('extract_audio'):
            ydl_opts['postprocessors'] = [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': options.get('audio_format', 'mp3'),
                'preferredquality': options.get('audio_quality', '192'),
            }]
        
        # Embed options
        if options.get('embed_thumbnail'):
            ydl_opts.setdefault('postprocessors', []).append({
                'key': 'EmbedThumbnail',
            })
        
        if options.get('embed_metadata'):
            ydl_opts.setdefault('postprocessors', []).append({
                'key': 'FFmpegMetadata',
            })
        
        # Subtitle options
        if options.get('download_subtitles'):
            ydl_opts['writesubtitles'] = True
            ydl_opts['subtitleslangs'] = options.get('subtitle_languages', ['en'])
            ydl_opts['subtitlesformat'] = options.get('subtitle_format', 'srt')
        
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)
                
                # Get the downloaded file path
                filename = ydl.prepare_filename(info)
                
                # If audio was extracted, update extension
                if options.get('extract_audio'):
                    filename = os.path.splitext(filename)[0] + f".{options.get('audio_format', 'mp3')}"
                # If merged, the output will be in merge_output_format
                elif options.get('merge_output_format'):
                    filename = os.path.splitext(filename)[0] + f".{options['merge_output_format']}"
                
                return {
                    'success': True,
                    'filepath': filename,
                    'title': info.get('title', 'Unknown'),
                    'filesize': os.path.getsize(filename) if os.path.exists(filename) else 0
                }
                
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }
    
    def _progress_hook(self, d: Dict):
        """Hook for progress updates"""
        if self.is_cancelled:
            raise Exception("Download cancelled by user")
        
        if self.progress_callback:
            status = d.get('status')
            
            if status == 'downloading':
                progress_info = {
                    'status': 'downloading',
                    'downloaded_bytes': d.get('downloaded_bytes', 0),
                    'total_bytes': d.get('total_bytes') or d.get('total_bytes_estimate', 0),
                    'speed': d.get('speed', 0),
                    'eta': d.get('eta', 0),
                    'percent': d.get('downloaded_bytes', 0) / max(d.get('total_bytes', 1), 1) * 100
                }
                self.progress_callback(progress_info)
            
            elif status == 'finished':
                self.progress_callback({
                    'status': 'finished',
                    'filename': d.get('filename', '')
                })
    
    def cancel(self):
        """Cancel ongoing download"""
        self.is_cancelled = True


class PlaylistExtractor:
    """Extract videos from playlists"""
    
    @staticmethod
    def extract_playlist_urls(playlist_url: str) -> tuple[list[str], dict]:
        """
        Extract all video URLs from a playlist
        Returns: (video_urls, playlist_info)
        """
        ydl_opts = {
            'quiet': True,
            'extract_flat': True,
            'skip_download': True,
        }
        
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(playlist_url, download=False)
                
                if not info or 'entries' not in info:
                    return [], {}
                
                # Extract video URLs
                urls = []
                for entry in info['entries']:
                    if entry:
                        video_id = entry.get('id')
                        url = entry.get('url') or entry.get('webpage_url')
                        if not url and video_id:
                            # Construct URL from ID (YouTube specific)
                            url = f"https://youtube.com/watch?v={video_id}"
                        if url:
                            urls.append(url)
                
                playlist_info = {
                    'title': info.get('title', 'Unknown Playlist'),
                    'uploader': info.get('uploader', 'Unknown'),
                    'video_count': len(urls),
                    'description': info.get('description', '')
                }
                
                return urls, playlist_info
                
        except Exception as e:
            print(f"Error extracting playlist: {e}")
            return [], {}
