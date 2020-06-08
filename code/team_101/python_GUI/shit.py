# -*- coding: utf-8 -*-
import os

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
            print "gazebo wrong again uh oh"
            print i
            return False
    print "gazebo right"
    return True

check_gazebo()
