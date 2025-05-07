from pytube import YouTube
video_url = "https://www.youtube.com/watch?v=hKQNL-6CdBo"
yt = YouTube(video_url)
print(yt.title)
