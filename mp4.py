import youtube_dl

ydl_opts = {
    'format': 'mp4',
}

ydl =  youtube_dl.YoutubeDL(ydl_opts)

url = input("Vid to dl?  ")

ydl.download([url])

