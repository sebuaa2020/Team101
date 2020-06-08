# -*- coding: utf-8 -*-
import os
import signal
import PIL.Image
import PIL.ImageTk
import time
import matplotlib.pyplot as plt
import pylab
import subprocess
import numpy as np
from motion import *
from ExceptionHandler import *
from datetime import datetime
dt=datetime.now() 
NORMAL = 1

def check_gazebo():
    list =  ['/clock', '/cmd_vel', '/gazebo/link_states', '/gazebo/model_states', '/gazebo/parameter_descriptions', 
            '/gazebo/parameter_updates', '/gazebo/set_link_state', '/gazebo/set_model_state', 
            '/gazebo_gui/parameter_descriptions', '/gazebo_gui/parameter_updates', '/kinect2/hd/camera_info', 
            '/kinect2/hd/image_color_rect', '/kinect2/hd/parameter_descriptions', '/kinect2/hd/parameter_updates',
            '/kinect2/sd/camera_info', '/kinect2/sd/depth/camera_info', '/kinect2/sd/image_depth_rect', 
            '/kinect2/sd/image_ir_rect', '/kinect2/sd/parameter_descriptions', '/kinect2/sd/parameter_updates',
            '/kinect2/sd/points', '/odom', '/rosout', '/rosout_agg', '/scan', '/tf']

    command = 'rostopic list' #可以直接在命令行中执行的命令
    r = os.popen(command) #执行该命令
    info = r.readlines() #读取命令行的输出到一个list
    cur = []
    for line in info: #按行遍历
        line = line.strip('\r\n')
        cur.append(line)
    
    for i in list:
        if i not in cur:
            return False
    return True

def check_rviz():
    list =  ['/clicked_point', '/clock', '/cmd_vel', '/gazebo/link_states', '/gazebo/model_states', '/gazebo/parameter_descriptions', 
            '/gazebo/parameter_updates', '/gazebo/set_link_state', '/gazebo/set_model_state', '/initialpose', '/joint_states', '/joy',
            '/gazebo_gui/parameter_descriptions', '/gazebo_gui/parameter_updates', '/kinect2/hd/camera_info', 
            '/kinect2/hd/image_color_rect', '/kinect2/hd/parameter_descriptions', '/kinect2/hd/parameter_updates',
            '/kinect2/sd/camera_info', '/kinect2/sd/depth/camera_info', '/kinect2/sd/image_depth_rect', 
            '/kinect2/sd/image_ir_rect', '/kinect2/sd/parameter_descriptions', '/kinect2/sd/parameter_updates',
            '/kinect2/sd/points', '/odom', '/rosout', '/rosout_agg', '/scan', '/tf', '/tf_static', '/slam_gmapping/entropy']

    command = 'rostopic list' #可以直接在命令行中执行的命令
    r = os.popen(command) #执行该命令
    info = r.readlines() #读取命令行的输出到一个list
    cur = []
    for line in info: #按行遍历
        line = line.strip('\r\n')
        cur.append(line)
    
    for i in list:
        if i not in cur:
            return False
    return True

class Map:
    def __init__(self):
        self.robot = 0
        self.hector_slam = 0
        self.keyboard = 0
        self.built = 0
        self.log = 0

    def buildMap(self, log):
        self.log = log
        self.built = 1
        # spawn机器人
        self.log.insert("insert", dt.strftime( '%y-%m-%d %I:%M:%S %p [程序运行] Gazebo启动机器人\n' ))
        self.robot = subprocess.Popen(['gnome-terminal', '--disable-factory', '-e', 'bash  -c \"roslaunch team_101 robot_spawn.launch; exec bash\"'],
                            preexec_fn=os.setpgrp)
        
        time.sleep(10)
        while check_gazebo() is False:
        
            os.killpg(self.robot.pid, signal.SIGINT)
            time.sleep(5)
            self.log.insert("insert", dt.strftime( '%y-%m-%d %I:%M:%S %p [报错] Gazebo启动失败！自动重启！\n' ))
            print "gazebo启动失败"
            self.log.insert("insert", dt.strftime( '%y-%m-%d %I:%M:%S %p [程序运行] Gazebo启动机器人\n' ))
            self.robot = subprocess.Popen(['gnome-terminal', '--disable-factory', '-e', 'bash  -c \"roslaunch team_101 robot_spawn.launch; exec bash\"'],
                            preexec_fn=os.setpgrp)
            time.sleep(10)

        # 开始建图
        self.log.insert("insert", dt.strftime( '%y-%m-%d %I:%M:%S %p [程序运行] Rviz启动机器人\n' ))
        self.hector_slam = subprocess.Popen(['gnome-terminal', '--disable-factory', '-e', 'bash -c \"roslaunch team_101 gmapping.launch; exec bash\"'],
                            preexec_fn=os.setpgrp)
        time.sleep(10)
        while check_rviz() is False:
        
            os.killpg(self.hector_slam.pid, signal.SIGINT)
            time.sleep(5)
            self.log.insert("insert", dt.strftime( '%y-%m-%d %I:%M:%S %p [报错] Rviz启动失败！自动重启！\n' ))
            print "rviz启动失败"
            self.log.insert("insert", dt.strftime( '%y-%m-%d %I:%M:%S %p [程序运行] Rviz启动机器人\n' ))
            self.hector_slam = subprocess.Popen(['gnome-terminal', '--disable-factory', '-e', 'bash -c \"roslaunch team_101 gmapping.launch; exec bash\"'],
                            preexec_fn=os.setpgrp)
            time.sleep(10)

        #self.log.insert("insert", dt.strftime( '%y-%m-%d %I:%M:%S %p [动作] Gazebo启动机器人\n' ))
        #self.keyboard = subprocess.Popen(['gnome-terminal', '--disable-factory', '-e', 'bash -c \"rosrun team_101 keyboard_ctrl; exec bash\"'],
        #                   preexec_fn=os.setpgrp)


    def saveMap(self):
        # 保存地图 
        #print "建图结束，自动保存地图"
        #print "……………………………………"
        self.log.insert("insert", dt.strftime( '\n%y-%m-%d %I:%M:%S %p [操作] 保存地图\n' ))
        p_temp = subprocess.Popen('rosrun map_server map_saver -f map', shell=True)
        p_temp.wait()
        # os.system("gnome-terminal -e 'bash -c \"cp ~/map.pgm ~/catkin_ws/src/team_101/maps/\"'")
        p_temp = subprocess.Popen('cp map.pgm ~/catkin_ws/src/team_101/maps/', shell=True)
        p_temp.wait()
        p_temp = subprocess.Popen('rm -f map.pgm', shell=True)
        p_temp.wait()
        # os.system("gnome-terminal -e 'bash -c \"cp ~/map.yaml ~/catkin_ws/src/team_101/maps/\"'")
        p_temp = subprocess.Popen('cp map.yaml ~/catkin_ws/src/team_101/maps/', shell=True)
        p_temp.wait()
        p_temp = subprocess.Popen('rm -f map.yaml', shell=True)
        p_temp.wait()
        time.sleep(10)
        os.killpg(self.hector_slam.pid, signal.SIGINT)
        os.killpg(self.robot.pid, signal.SIGINT)
        # os.killpg(self.keyboard.pid, signal.SIGINT)
        

    def getMap(self):#从指定路径获取地图
        
        path = os.getcwd() + '\maps\map.pgm'
        try:
            im = PIL.Image.open(path)
            self.log.insert("insert", dt.strftime( '%y-%m-%d %I:%M:%S %p [操作] 从' ))
            self.log.insert("insert", path)
            self.log.insert("insert", "读取地图" )
        except ValueError:
            self.log.insert("insert", dt.strftime( '%y-%m-%d %I:%M:%S %p [报错] 从' ))
            self.log.insert("insert", path)
            self.log.insert("insert", "读取地图失败" )
        return im

    def mapException(self): #处理建图过程中的异常
        error = Exception(0,'')
        error.ExceptionHandler()




