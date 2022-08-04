import youtube_dl

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

ydl =  youtube_dl.YoutubeDL(ydl_opts)

url = input("Vid to dl?  ")

ydl.download([url])

