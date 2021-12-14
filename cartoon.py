import os
import time
import subprocess
from random import *

directory = "some_dir"

while True:
    for root, subdirectories, files in os.walk(directory):
        rng = randint(0, len(subdirectories) - 1)
        sub = subdirectories[rng]
        new_dir = directory + "\\" + sub
        for root1, subdirectories1, files1 in os.walk(new_dir):
            rng1 = randint(0, len(files1) - 1)
            file = files1[rng1]
            kappa = new_dir + "\\" + file
            print(kappa)
            p = subprocess.Popen(["C:\\Program Files (x86)\\VideoLAN\\VLC\\vlc.exe", kappa])
            while p.poll() is None:
                time.sleep(1)
            if p.poll() is not None:
                break
            break
        break
