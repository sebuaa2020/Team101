from tkinter import *
import os
import signal
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
        # spawn机器人
        print "机器人启动"
        print "……………………………………"
        # os.system("gnome-terminal -e 'bash -c \"roslaunch robot_sim_demo robot_spawn.launch; exec bash\"'")

        robot = subprocess.Popen(['gnome-terminal', '--disable-factory', '-e', 'bash  -c \"roslaunch robot_sim_demo robot_spawn.launch; exec bash\"'],
                            preexec_fn=os.setpgrp)
        time.sleep(10)

        # 开始建图
        print "开始建图"
        print "……………………………………"
        hector_slam = subprocess.Popen(['gnome-terminal', '--disable-factory', '-e', 'bash -c \"roslaunch wpb_home_tutorials hector_mapping.launch; exec bash\"'],
                            preexec_fn=os.setpgrp)

        '''

        移动机器人

        '''

        time.sleep(10)
        os.killpg(hector_slam.pid, signal.SIGINT)

        # 保存地图 
        print "建图结束，自动保存地图"
        print "……………………………………"

        p_temp = subprocess.Popen('rosrun map_server map_saver -f map', shell=True)
        p_temp.wait()
        os.system("gnome-terminal -e 'bash -c \"cp ~/map.pgm ~/catkin_ws/src/team_101/maps/\"'")
        p_temp.wait()
        os.system("gnome-terminal -e 'bash -c \"cp ~/map.yaml ~/catkin_ws/src/team_101/maps/\"'")
        p_temp.wait()


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


