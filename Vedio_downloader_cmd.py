import yt_dlp

def download_video(video_url, download_path,progress_hook=None):
    ydl_opts = {
        'outtmpl': f'{download_path}/%(title)s.%(ext)s',  # Save to chosen folder
        'format': 'bestvideo+bestaudio/best',             # Best quality
        'merge_output_format': 'mp4',                    # Merge to mp4 if possible
    }
    if progress_hook:
        ydl_opts['progress_hooks'] = [progress_hook]
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])
