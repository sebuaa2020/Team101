# -*- coding: utf-8 -*-
import os
import signal
import subprocess
import time
from datetime import datetime

dt=datetime.now() #创建一个datetime类对象

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
    list =  ['/amcl/parameter_descriptions', '/amcl/parameter_updates', '/amcl_pose', '/clicked_point', '/clock', '/cmd_vel', '/gazebo/link_states', '/gazebo/model_states',
            '/gazebo/parameter_descriptions', '/gazebo/parameter_updates', '/gazebo/set_link_state', '/gazebo/set_model_state', '/gazebo_gui/parameter_descriptions', '/gazebo_gui/parameter_updates', 
            '/initialpose', '/joint_states', '/kinect2/hd/camera_info', '/kinect2/hd/image_color_rect', '/kinect2/hd/parameter_descriptions', '/kinect2/hd/parameter_updates', '/kinect2/qhd/points', 
            '/kinect2/sd/camera_info', '/kinect2/sd/depth/camera_info', '/kinect2/sd/image_depth_rect', '/kinect2/sd/image_ir_rect', '/kinect2/sd/parameter_descriptions', '/kinect2/sd/parameter_updates', 
            '/kinect2/sd/points', '/map', '/map_metadata', '/map_updates', '/move_base/DWAPlannerROS/cost_cloud', '/move_base/DWAPlannerROS/global_plan', '/move_base/DWAPlannerROS/local_plan', 
            '/move_base/DWAPlannerROS/parameter_descriptions', '/move_base/DWAPlannerROS/parameter_updates', '/move_base/DWAPlannerROS/trajectory_cloud', '/move_base/GlobalPlanner/parameter_descriptions',
            '/move_base/GlobalPlanner/parameter_updates', '/move_base/GlobalPlanner/plan', '/move_base/GlobalPlanner/potential', '/move_base/cancel', '/move_base/current_goal', '/move_base/feedback', 
            '/move_base/global_costmap/costmap', '/move_base/global_costmap/costmap_updates', '/move_base/global_costmap/footprint', '/move_base/global_costmap/inflation_layer/parameter_descriptions', 
            '/move_base/global_costmap/inflation_layer/parameter_updates', '/move_base/global_costmap/obstacle_layer/parameter_descriptions', '/move_base/global_costmap/obstacle_layer/parameter_updates', 
            '/move_base/global_costmap/parameter_descriptions', '/move_base/global_costmap/parameter_updates', '/move_base/global_costmap/static_layer/parameter_descriptions', 
            '/move_base/global_costmap/static_layer/parameter_updates', '/move_base/goal', '/move_base/local_costmap/costmap', '/move_base/local_costmap/costmap_updates', '/move_base/local_costmap/footprint', 
            '/move_base/local_costmap/inflation_layer/parameter_descriptions', '/move_base/local_costmap/inflation_layer/parameter_updates', '/move_base/local_costmap/obstacle_layer/parameter_descriptions', 
            '/move_base/local_costmap/obstacle_layer/parameter_updates', '/move_base/local_costmap/parameter_descriptions', '/move_base/local_costmap/parameter_updates', '/move_base/parameter_descriptions', 
            '/move_base/parameter_updates', '/move_base/result', '/move_base/status', '/move_base_simple/goal', '/odom', '/particlecloud', '/rosout', '/rosout_agg', '/scan', '/tf', '/tf_static', 
            '/visualization_marker', '/visualization_marker_array', '/waypoints_marker', '/waypoints_marker_array']

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
        while check_gazebo() is False:
            os.killpg(self.robot.pid, signal.SIGINT)
            time.sleep(5)
            self.log.insert("insert", dt.strftime( '%y-%m-%d %I:%M:%S %p [报错] Gazebo启动失败！自动重启！\n' ))
            print "gazebo启动失败"
            self.log.insert("insert", dt.strftime( '%y-%m-%d %I:%M:%S %p [程序运行] Gazebo启动机器人\n' ))
            self.robot = subprocess.Popen(['gnome-terminal', '--disable-factory', '-e', 'bash  -c \"roslaunch team_101 robot_spawn.launch; exec bash\"'],
                            preexec_fn=os.setpgrp)
            time.sleep(10)

        self.log.insert("insert", dt.strftime( '%y-%m-%d %I:%M:%S %p [程序运行] Rviz启动地图场景\n' ))
        self.navi = subprocess.Popen(['gnome-terminal', '--disable-factory', '-e',
                          'bash -c \"roslaunch team_101 navigation.launch; exec bash\"'],
                         preexec_fn=os.setpgrp)
        time.sleep(10)
        while check_rviz() is False:
        
            os.killpg(self.navi, signal.SIGINT)
            time.sleep(5)
            self.log.insert("insert", dt.strftime( '%y-%m-%d %I:%M:%S %p [报错] Rviz启动失败！自动重启！\n' ))
            print "rviz启动失败"
            self.log.insert("insert", dt.strftime( '%y-%m-%d %I:%M:%S %p [程序运行] Rviz启动机器人\n' ))
            self.navi = subprocess.Popen(['gnome-terminal', '--disable-factory', '-e',
                          'bash -c \"roslaunch team_101 navigation.launch; exec bash\"'],preexec_fn=os.setpgrp)
            time.sleep(10)

        self.log.insert("insert", dt.strftime( '%y-%m-%d %I:%M:%S %p [过程] 开始导航\n' ))
        

    def endMove(self): #停止导航过程，关闭窗口
        os.killpg(self.robot.pid, signal.SIGINT)
        os.killpg(self.navi.pid, signal.SIGINT)
        self.log.insert("insert", dt.strftime( '%y-%m-%d %I:%M:%S %p [过程] 结束导航\n' ))
