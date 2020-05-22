# -*- coding: utf-8 -*-
from Tkinter import *
import os
import signal
from PIL import Image, ImageTk
import time
import matplotlib.pyplot as plt
import pylab
import subprocess
import numpy as np
from motion import *
global finishBM
NORMAL = 1
finishBM = False
class Map:
    im = np.zeros((255,255))
    message_queue = list

    def buildMap(self):
        # spawn机器人
        robot = subprocess.Popen(['gnome-terminal', '--disable-factory', '-e', 'bash  -c \"roslaunch robot_sim_demo robot_spawn.launch; exec bash\"'],
                            preexec_fn=os.setpgrp)
        time.sleep(10)
        
        # 开始建图
        hector_slam = subprocess.Popen(['gnome-terminal', '--disable-factory', '-e', 'bash -c \"roslaunch wpb_home_tutorials hector_mapping.launch; exec bash\"'],
                            preexec_fn=os.setpgrp)


        # todo: 移动机器人
        while True:
            if finishBM:
                break

        os.killpg(hector_slam.pid, signal.SIGINT)

        # 保存地图 
        print "建图结束，自动保存地图"
        print "……………………………………"

        p_temp = subprocess.Popen('rosrun map_server map_saver -f map', shell=True)
        p_temp.wait()
        # os.system("gnome-terminal -e 'bash -c \"cp ~/map.pgm ~/catkin_ws/src/team_101/maps/\"'")
        subprocess.Popen('cp map.pgm ~/catkin_ws/src/team_101/maps/\\', shell=True)
        subprocess.Popen('rm -f map.pgm', shell=True)
        # os.system("gnome-terminal -e 'bash -c \"cp ~/map.yaml ~/catkin_ws/src/team_101/maps/\"'")
        subprocess.Popen('cp map.yaml ~/catkin_ws/src/team_101/maps/\\', shell=True)
        subprocess.Popen('rm -f map.yaml', shell=True)
        

    def getMap(self):#从指定路径获取地图
        path = os.getcwd() + '\maps\map.pgm'
        im = Image.open(path)
        return im

    def mapException(self): #处理建图过程中的异常
        os.system("gnome-terminal -e 'bash -c \"rosrun move stop; exec bash\"'")

    def getMessage(self, STATE):
        if STATE != NORMAL:
            return 1
        else :
            return 0


