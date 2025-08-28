# Multithreading - multitasking

import threading
import time

def walk_dog(dog):
    time.sleep(8)
    print(f"You finish walking the {dog}.")

def take_out_trash(trash1, trash2):
    time.sleep(2)
    print(f"You take out the {trash1} and {trash2}.")

def get_mail():
    time.sleep(4)
    print("You get the mail.")

# walk_dog()
# take_out_trash()
# get_mail()

chore1 = threading.Thread(target=walk_dog, args=("Gucci",))                 # , parodo kad sunciam tuple, jeigu tik vienas argumentas
chore1.start()

chore2 = threading.Thread(target=take_out_trash, args=("plastic", "glass"))
chore2.start()

chore3 = threading.Thread(target=get_mail)
chore3.start()

chore1.join()
chore2.join()
chore3.join()
print("All chores are complete!")