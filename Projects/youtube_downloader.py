from pytubefix import YouTube
import tkinter as tk
from tkinter import filedialog

def download_video(url, save_path):
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True, file_extension="mp4")
        video = streams.get_highest_resolution()
        if not video:
            print("720p not available. Downloading best available quality...")
            video = streams.order_by("resolution").desc().first()
        video.download(output_path=save_path)
        print("Video downloaded successfully!")

    except Exception as e:
        print(e)

url = "https://www.youtube.com/shorts/XinUJXQPo38"
save_path = "C:/Users/vaida/Downloads"

download_video(url, save_path)