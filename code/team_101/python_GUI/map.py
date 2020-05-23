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

NORMAL = 1

class Map:
    def __init__(self):
        im = np.zeros((255,255))
        message_queue = list
        self.robot = 0
        self.hector_slam = 0

    def buildMap(self):
        # spawn机器人
        self.robot = subprocess.Popen(['gnome-terminal', '--disable-factory', '-e', 'bash  -c \"roslaunch team_101 robot_spawn.launch; exec bash\"'],
                            preexec_fn=os.setpgrp)
        time.sleep(10)
        
        # 开始建图
        self.hector_slam = subprocess.Popen(['gnome-terminal', '--disable-factory', '-e', 'bash -c \"roslaunch team_101 gmapping.launch; exec bash\"'],
                            preexec_fn=os.setpgrp)


    def saveMap(self):

        # 保存地图 
        print "建图结束，自动保存地图"
        print "……………………………………"

        p_temp = subprocess.Popen('rosrun map_server map_saver -f map', shell=True)
        p_temp.wait()
        # os.system("gnome-terminal -e 'bash -c \"cp ~/map.pgm ~/catkin_ws/src/team_101/maps/\"'")
        p_temp = subprocess.Popen('cp map.pgm ~/catkin_ws/src/team_101/python_GUI/maps/', shell=True)
        p_temp.wait()
        p_temp = subprocess.Popen('rm -f map.pgm', shell=True)
        p_temp.wait()
        # os.system("gnome-terminal -e 'bash -c \"cp ~/map.yaml ~/catkin_ws/src/team_101/maps/\"'")
        p_temp = subprocess.Popen('cp map.yaml ~/catkin_ws/src/team_101/python_GUI/maps/', shell=True)
        p_temp.wait()
        p_temp = subprocess.Popen('rm -f map.yaml', shell=True)
        p_temp.wait()
        time.sleep(10)
        os.killpg(self.hector_slam.pid, signal.SIGINT)
        os.killpg(self.robot.pid, signal.SIGINT)
        

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


