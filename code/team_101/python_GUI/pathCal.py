# -*- coding: utf-8 -*-
import os
import signal
import subprocess
import time

class pathCal:
    def __init__(self):
        self.path = ''
        self.robot = 0
        self.navi = 0

    def move(self): #调用ROS包选取导航轨迹
        self.robot = subprocess.Popen(['gnome-terminal', '--disable-factory', '-e',
                          'bash  -c \"roslaunch team_101 robot_spawn.launch; exec bash\"'],
                         preexec_fn=os.setpgrp)
        time.sleep(10)
        self.navi = subprocess.Popen(['gnome-terminal', '--disable-factory', '-e',
                          'bash -c \"roslaunch team_101 navigation.launch; exec bash\"'],
                         preexec_fn=os.setpgrp)

    def endMove(self): #停止导航过程，关闭窗口
        os.killpg(self.robot.pid, signal.SIGINT)
        os.killpg(self.navi.pid, signal.SIGINT)
