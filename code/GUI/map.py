from tkinter import *
import os
from PIL import Image, ImageTk
import time
import matplotlib.pyplot as plt
import pylab
import subprocess
import numpy as np
NORMAL = 1
class map:
    im = np.zeros(255,255)
    message_queue = list
    def buildMap(self):
        os.system("gnome-terminal -e 'bash -c \"roslaunch wpr_simulation wpb_simple.launch; exec bash\"'")
        time.sleep(2)
        os.system("gnome-terminal -e 'bash -c \"roslaunch wpb_home_tutorials gmapping.launch; exec bash\"'")
        time.sleep(2)
        os.system("gnome-terminal -e 'bash -c \"rosrun wpr_simulation keyboard_vel_ctrl; exec bash\"'")
        time.sleep(2)
        os.system("gnome-terminal -e 'bash -c \"rosrun map_server map_saver -f map; exec bash\"'")


    def getMap(self):
        path = os.getcwd() + '\maps\map.pgm'
        im = Image.open(path)
        return im

    def mapException(self):
        os.system("gnome-terminal -e 'bash -c \"rosrun move stop; exec bash\"'")

    def getMessage(self, STATE):
        if STATE != NORMAL:
            return 1
        else :
            return 0


