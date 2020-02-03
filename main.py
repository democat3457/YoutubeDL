import youtube_dl
import os

ydl = youtube_dl.YoutubeDL({
    'outtmpl': 'media/%(title)s.%(ext)s',
    'format': 'bestvideo+bestaudio/best'
})

url = input("Video URL: ")

with ydl:
    result = ydl.extract_info(
        str(url),
        download=True
    )

if 'entries' in result:
    # Can be a playlist or a list of videos
    video = result['entries'][0]
else:
    # Just a video
    video = result

print(video)
title = video['title']
print(title)