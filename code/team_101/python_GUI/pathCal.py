# -*- coding: utf-8 -*-
import os
import signal
import subprocess
import time
from datetime import datetime

dt=datetime.now() #创建一个datetime类对象

class pathCal:
    def __init__(self,root,log):
        self.path = ''
        self.robot = 0
        self.navi = 0
        self.root = root
        self.log = log

    def move(self): #调用ROS包选取导航轨迹
        self.log.insert("insert", dt.strftime( '%y-%m-%d %I:%M:%S %p [程序运行] Gazebo启动机器人\n' ))
        self.robot = subprocess.Popen(['gnome-terminal', '--disable-factory', '-e',
                          'bash  -c \"roslaunch team_101 robot_spawn.launch; exec bash\"'],
                         preexec_fn=os.setpgrp)
       
        time.sleep(10)
        self.log.insert("insert", dt.strftime( '%y-%m-%d %I:%M:%S %p [程序运行] Rviz启动地图场景\n' ))
        self.navi = subprocess.Popen(['gnome-terminal', '--disable-factory', '-e',
                          'bash -c \"roslaunch team_101 navigation.launch; exec bash\"'],
                         preexec_fn=os.setpgrp)
        self.log.insert("insert", dt.strftime( '%y-%m-%d %I:%M:%S %p [过程] 开始导航\n' ))
        

    def endMove(self): #停止导航过程，关闭窗口
        os.killpg(self.robot.pid, signal.SIGINT)
        os.killpg(self.navi.pid, signal.SIGINT)
        self.log.insert("insert", dt.strftime( '%y-%m-%d %I:%M:%S %p [过程] 结束导航\n' ))
