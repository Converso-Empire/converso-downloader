"""Format processing and categorization for Converso Pro Downloader"""

from typing import Dict, List, Optional


class FormatProcessor:
    """Process and categorize available formats"""
    
    @staticmethod
    def categorize_formats(formats: List[dict]) -> Dict[str, List[dict]]:
        """
        Categorize formats by type
        Returns: {
            'video_only': list[dict],
            'audio_only': list[dict],
            'progressive': list[dict],
        }
        """
        categorized = {
            'video_only': [],
            'audio_only': [],
            'progressive': []
        }
        
        for fmt in formats:
            vcodec = fmt.get('vcodec', 'none')
            acodec = fmt.get('acodec', 'none')
            
            if vcodec != 'none' and acodec != 'none':
                # Has both video and audio
                categorized['progressive'].append(fmt)
            elif vcodec != 'none' and acodec == 'none':
                # Video only
                categorized['video_only'].append(fmt)
            elif vcodec == 'none' and acodec != 'none':
                # Audio only
                categorized['audio_only'].append(fmt)
        
        return categorized
    
    @staticmethod
    def sort_by_quality(formats: List[dict], format_type: str) -> List[dict]:
        """
        Sort formats by quality (resolution/bitrate)
        format_type: 'video' or 'audio'
        """
        if format_type == 'video':
            # Sort by height (resolution), then fps, then bitrate
            return sorted(
                formats,
                key=lambda x: (
                    x.get('height', 0),
                    x.get('fps', 0),
                    x.get('tbr', 0) or x.get('vbr', 0) or 0
                ),
                reverse=True
            )
        else:  # audio
            # Sort by bitrate, then sample rate
            return sorted(
                formats,
                key=lambda x: (
                    x.get('abr', 0) or x.get('tbr', 0) or 0,
                    x.get('asr', 0)
                ),
                reverse=True
            )
    
    @staticmethod
    def get_format_label(format_dict: dict) -> str:
        """
        Generate human-readable format label
        e.g., "1080p60 • VP9 • 850MB"
        """
        parts = []
        
        # Resolution
        if height := format_dict.get('height'):
            resolution = f"{height}p"
            if (fps := format_dict.get('fps', 30)) > 30:
                resolution += f"{fps}"
            parts.append(resolution)
        
        # Codec
        if vcodec := format_dict.get('vcodec'):
            if vcodec != 'none':
                codec = vcodec.split('.')[0].upper()
                parts.append(codec[:10])
        
        if acodec := format_dict.get('acodec'):
            if acodec != 'none' and not format_dict.get('vcodec'):
                codec = acodec.split('.')[0].upper()
                parts.append(codec[:10])
        
        # Size
        filesize = format_dict.get('filesize') or format_dict.get('filesize_approx', 0)
        if filesize:
            parts.append(FormatProcessor._format_bytes(filesize))
        
        # Bitrate for audio
        if abr := format_dict.get('abr'):
            parts.append(f"{int(abr)}kbps")
        
        return " • ".join(parts)
    
    @staticmethod
    def filter_formats(formats: List[dict], **criteria) -> List[dict]:
        """
        Filter formats by criteria:
        - min_height, max_height
        - min_bitrate, max_bitrate
        - codecs (list of preferred codecs)
        - extensions (list of preferred extensions)
        """
        filtered = formats.copy()
        
        if min_height := criteria.get('min_height'):
            filtered = [f for f in filtered if f.get('height', 0) >= min_height]
        
        if max_height := criteria.get('max_height'):
            filtered = [f for f in filtered if f.get('height', 9999) <= max_height]
        
        if min_bitrate := criteria.get('min_bitrate'):
            filtered = [f for f in filtered 
                       if (f.get('tbr', 0) or f.get('vbr', 0) or f.get('abr', 0)) >= min_bitrate]
        
        if max_bitrate := criteria.get('max_bitrate'):
            filtered = [f for f in filtered 
                       if (f.get('tbr', 0) or f.get('vbr', 0) or f.get('abr', 0)) <= max_bitrate]
        
        if codecs := criteria.get('codecs'):
            filtered = [f for f in filtered 
                       if any(codec.lower() in (f.get('vcodec', '') + f.get('acodec', '')).lower() 
                             for codec in codecs)]
        
        if extensions := criteria.get('extensions'):
            filtered = [f for f in filtered if f.get('ext') in extensions]
        
        return filtered
    
    @staticmethod
    def _format_bytes(bytes_size: int) -> str:
        """Format bytes to human-readable size"""
        if not bytes_size or bytes_size <= 0:
            return "?"
        
        for unit in ['B', 'KB', 'MB', 'GB']:
            if bytes_size < 1024.0:
                return f"{bytes_size:.0f}{unit}"
            bytes_size /= 1024.0
        return f"{bytes_size:.0f}TB"
    
    @staticmethod
    def get_best_format_id(formats: List[dict], quality: str = 'best') -> Optional[str]:
        """
        Get the best format ID based on quality preference
        quality: 'best', 'high', 'medium', 'low'
        """
        if not formats:
            return None
        
        categorized = FormatProcessor.categorize_formats(formats)
        video_formats = FormatProcessor.sort_by_quality(categorized['video_only'], 'video')
        
        if not video_formats:
            # Try progressive formats
            video_formats = FormatProcessor.sort_by_quality(categorized['progressive'], 'video')
        
        if not video_formats:
            return None
        
        quality_map = {
            'best': 0,  # Index 0 = highest quality
            'high': min(len(video_formats) // 4, len(video_formats) - 1),
            'medium': min(len(video_formats) // 2, len(video_formats) - 1),
            'low': min(3 * len(video_formats) // 4, len(video_formats) - 1)
        }
        
        index = quality_map.get(quality, 0)
        return video_formats[index]['format_id']
