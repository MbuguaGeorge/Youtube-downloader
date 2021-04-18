import pytube
from pytube.cli import on_progress

print ('enter YouTube link')
link = input()
yt = pytube.YouTube(link, on_progress_callback=on_progress)
stream = yt.streams.first()
stream.download()