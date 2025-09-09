from pytubefix import YouTube
import tkinter as tk
from tkinter import filedialog

def download_video(url, save_path):
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True, file_extension="mp4")
        video = streams.get_highest_resolution()
        if not video:
            print("Downloading best available quality...")
            video = streams.order_by("resolution").desc().first()
        video.download(output_path=save_path)
        print("Video downloaded successfully!")

    except Exception as e:
        print(e)

def open_file_dialog():   
    root = tk.Tk()
    root.withdraw()
    root.lift()
    root.attributes('-topmost', True)      
 
    folder = filedialog.askdirectory(title="Select a folder to save the video")
    root.after_idle(root.attributes, '-topmost', False)
    root.destroy()
    if folder:
        print(f"Selected folder: {folder}")
    return folder

if __name__ == "__main__":
    
    video_url = input("Please enter a Youtube url: ")
    save_dir = open_file_dialog()

    if not save_dir:
        print("Invalid save location!")
    else:
        print("Downloading best available quality...")
        download_video(video_url, save_dir)