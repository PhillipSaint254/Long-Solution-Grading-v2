import yt_dlp
url = "https://www.youtube.com/watch?v=hKQNL-6CdBo"  # Example video
ydl = yt_dlp.YoutubeDL({'format': 'bestaudio/best'})
info_dict = ydl.extract_info(url, download=False)
title = info_dict.get('title', None)
print("Title:", title, "duration:", info_dict.get('duration'))
