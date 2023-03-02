from pytube import YouTube
from sys import argv

link = argv[0]
yt = YouTube(link)

print("Title: ", yt.title)

yd = yt.streams.get_highest_resolution()

yd.download("~/Pobrane")

