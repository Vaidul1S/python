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

# url = "https://www.youtube.com/shorts/XinUJXQPo38"
# save_path = "C:/Users/vaida/Downloads"

# download_video(url, save_path)

def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected folder: {folder}")
    return folder

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    video_url = input("Please enter a Youtube url: ")
    save_dir = open_file_dialog()

    if not save_dir:
        print("Invalid save location!")
    else:
        download_video(video_url, save_dir)