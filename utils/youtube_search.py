"""YouTube search and video lookup functionality"""

import yt_dlp
from typing import List, Dict, Optional


class YouTubeSearcher:
    """Search YouTube videos and extract information"""
    
    def __init__(self):
        self.ydl_opts = {
            'quiet': True,
            'no_warnings': True,
            'extract_flat': 'in_playlist',  # Extract more info while keeping it fast
            'skip_download': True,
        }
    
    def search(self, query: str, max_results: int = 10) -> List[Dict]:
        """
        Search YouTube for videos
        Returns list of video information
        """
        if not query or not query.strip():
            return []
        
        query = query.strip()
        
        # If it's already a URL, return it
        if query.startswith('http://') or query.startswith('https://'):
            return [{'url': query, 'type': 'direct_url'}]
        
        # If it's a video ID (11 characters), convert to URL
        if len(query) == 11 and query.replace('-', '').replace('_', '').isalnum():
            return [{'url': f'https://www.youtube.com/watch?v={query}', 'type': 'video_id'}]
        
        # Otherwise, search YouTube
        search_query = f"ytsearch{max_results}:{query}"
        
        try:
            with yt_dlp.YoutubeDL(self.ydl_opts) as ydl:
                result = ydl.extract_info(search_query, download=False)
                
                if not result or 'entries' not in result:
                    return []
                
                videos = []
                for entry in result['entries']:
                    if entry:
                        # Get thumbnail - handle both string and list formats
                        thumbnail = entry.get('thumbnail', '')
                        if not thumbnail and entry.get('thumbnails'):
                            thumbnails = entry.get('thumbnails', [])
                            if isinstance(thumbnails, list) and thumbnails:
                                # Get the highest quality thumbnail
                                thumbnail = thumbnails[-1].get('url', '') if thumbnails else ''
                        
                        # If still no thumbnail, construct from video ID
                        if not thumbnail and entry.get('id'):
                            thumbnail = f"https://i.ytimg.com/vi/{entry.get('id')}/hqdefault.jpg"
                        
                        video = {
                            'id': entry.get('id', ''),
                            'title': entry.get('title', 'Unknown Title'),
                            'url': entry.get('url', '') or f"https://www.youtube.com/watch?v={entry.get('id', '')}",
                            'duration': entry.get('duration', 0),
                            'uploader': entry.get('uploader', 'Unknown'),
                            'view_count': entry.get('view_count', 0),
                            'thumbnail': thumbnail,
                            'type': 'search_result'
                        }
                        videos.append(video)
                
                return videos
                
        except Exception as e:
            print(f"Search error: {e}")
            return []
    
    def get_video_suggestions(self, query: str) -> List[str]:
        """
        Get video title suggestions based on search
        Returns list of video titles
        """
        results = self.search(query, max_results=5)
        return [video['title'] for video in results if video.get('title')]
    
    def parse_input(self, user_input: str) -> Dict:
        """
        Parse user input and determine what type it is
        Returns: dict with type and processed value
        """
        if not user_input or not user_input.strip():
            return {'type': 'empty', 'value': ''}
        
        user_input = user_input.strip()
        
        # Check if it's a URL
        if user_input.startswith('http://') or user_input.startswith('https://'):
            youtube_domains = ['youtube.com', 'youtu.be', 'm.youtube.com']
            if any(domain in user_input.lower() for domain in youtube_domains):
                return {'type': 'url', 'value': user_input}
            else:
                return {'type': 'invalid_url', 'value': user_input}
        
        # Check if it's a video ID (11 characters)
        if len(user_input) == 11 and user_input.replace('-', '').replace('_', '').isalnum():
            return {
                'type': 'video_id', 
                'value': user_input,
                'url': f'https://www.youtube.com/watch?v={user_input}'
            }
        
        # Otherwise it's a search query
        return {'type': 'search_query', 'value': user_input}
    
    def quick_lookup(self, user_input: str) -> Optional[str]:
        """
        Quick lookup to convert input to video URL
        Returns YouTube URL or None
        """
        parsed = self.parse_input(user_input)
        
        if parsed['type'] == 'url':
            return parsed['value']
        
        if parsed['type'] == 'video_id':
            return parsed['url']
        
        if parsed['type'] == 'search_query':
            # Get first search result
            results = self.search(parsed['value'], max_results=1)
            if results and len(results) > 0:
                return results[0]['url']
        
        return None
