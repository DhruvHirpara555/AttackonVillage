
import pickle as pkl
from src.screen import Screen

import time
import os
# ask file name to be replayed
import sys
replay_filename = input("Enter File name: ")

replay_file = open("./replay/" + replay_filename,'rb')

screens = pkl.load(replay_file)

replay_file.close()

print(len(screens))

framerate= 60
last_frame = time.time()
os.system('clear')

for i in range(len(screens)):


    sys.stdout.write(screens[i] + "\033[0;0H")
    time.sleep(1/framerate + 0.1)
    # move cursor to top left




