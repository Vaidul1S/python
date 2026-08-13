import os
import shutil
import datetime
import schedule
import time

source_dir = "/home/vaidulis/Pictures/Screenshots/"
destination_dir = "/home/vaidulis/Pictures/backups"

def copy_folder_to_direcion(source, dest):
    today = datetime.date.today()
    dest_dir = os.path.join(dest, str(today))

    try:
        shutil.copytree(source, dest_dir)
        print(f"Folder copied to: {dest_dir}")
    except FileExistsError:
        print(f"Folder already exists in: {dest}")
set_time = "10:47"
print(f"Copy will be executed at {set_time} o'clock")
schedule.every().day.at(set_time).do(lambda: copy_folder_to_direcion(source_dir, destination_dir))

while True:
    schedule.run_pending()
    time.sleep(60)