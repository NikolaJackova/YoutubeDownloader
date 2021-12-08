from pytube import YouTube
from pytube import Playlist
from moviepy.editor import *

class YoutubeDownloader:
    def convertMP4ToMP3(self, out_file):
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)

    def downloadVideo(self, link, path, mime_type):
        video_streams = YouTube(link).streams
        ys = video_streams.filter(only_video=False, mime_type=mime_type).first()
        out_file = ys.download(path)
        if "audio" in mime_type:
            self.convertMP4ToMP3(out_file)
    
    def download(self, link, path, type):
        mime_type = "audio/mp4"
        if "MP4" in type:
            mime_type = "video/mp4"
        playlist = Playlist(link)
        if len(playlist.video_urls) == 0:
            self.downloadVideo(link, path, mime_type)
        for item in playlist.video_urls:
            self.downloadVideo(item, path, mime_type)




