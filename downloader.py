from pytube import YouTube

link = input("Enter the link: ")
yt = YouTube(link)

ys = yt.streams.filter(only_audio=True).all()
ys[0].download()