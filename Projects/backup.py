import os
import shutil
import datetime
import schedule
import time

source_dir = "C:/Users/vaida/Pictures/Screenshots"
destination_dir = "C:/Users/vaida/Pictures/backups"

def copy_folder_to_direcion(source, dest):
    today = datetime.date.today()
    dest_dir = os.path.join(dest, str(today))

    try:
        shutil.copytree(source, dest_dir)
        print(f"Folder copied to: {dest_dir}")
    except FileExistsError:
        print(f"Folder already exists in: {dest}")

schedule.every().day.at("11:33").do(lambda: copy_folder_to_direcion(source_dir, destination_dir))

