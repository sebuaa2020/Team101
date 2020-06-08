# -*- coding: utf-8 -*-

import subprocess
import os
import threading
from Tkinter import *
from datetime import datetime
import rospy
from sensor_msgs.msg import LaserScan

ranges = []

def callback(scan):
    #LaserScan消息的格式
    #std_msgs/Header header
    #float32 angle_min
    #float32 angle_max
    #float32 angle_increment
    #float32 time_increment
    #float32 scan_time
    #float32 range_min
    #float32 range_max
    #float32[] ranges
    #float32[] intensities
    global ranges
    ranges = scan.ranges

def listener():
    rospy.init_node('laser_listener', anonymous=False, disable_signals=True)
    rospy.Subscriber('scan', LaserScan, callback)
    rospy.spin()

dt=datetime.now() #创建一个datetime类对象

class move: #基础运动

    def __init__(self, location, direction, speed,map):
        self.location = location
        self.direction = direction
        self.speed = speed
        self.map = map
        self.log = 0
        add_thread = threading.Thread(target = listener)
        add_thread.start()

    
    def link_log(self, log):
        self.log = log
    
    def set_status(self, status):
        self.map = status


    def obstruction_excepetion(self):
        error = Exception(1,self.direction)
        error.ExceptionHandler()

    def go_forward(self):
        if self.map == 1:
            self.log.insert("insert", dt.strftime( '%y-%m-%d %I:%M:%S %p [机器人动作] 向前移动\n' ))
            subprocess.Popen('rosrun team_101 go_forward', shell=True)
            global ranges
            min = 10
            for i in range(160, 210):
                print ranges[i]
                if len(ranges) > 0 and ranges[i] < 0.5 and ranges[i] < min:
                    min = ranges[i]
                    print min
                    
            if min != 10:
                self.log.insert("insert", dt.strftime( '%y-%m-%d %I:%M:%S %p [报错] 检测到近距离障碍物，距离' ))
                self.log.insert("insert", min)
                self.log.insert("insert", "米")
            else:
                self.log.insert("insert", dt.strftime( '%y-%m-%d %I:%M:%S %p [反馈] 机器人向前移动0.15米\n' ))

                    
        else:
            root = Tk()
            root.title('错误')
            root.geometry('300x80')
            lb = Label(root, text='当前没有建图程序在运行', \
                       fg='black', \
                       font=(25), \
                       width=30, \
                       height=2, \
                       relief=SUNKEN)
            lb.pack()
            root.mainloop()


    def go_backward(self):
        if self.map == 1:
            self.log.insert("insert", dt.strftime( '%y-%m-%d %I:%M:%S %p [机器人动作] 向后移动\n' ))
            subprocess.Popen('rosrun team_101 go_backward', shell=True)
            global ranges
            min = 10
            for i in range(330, 360):
                if len(ranges) > 0 and ranges[i] < 0.5 and ranges[i] < min:
                    min = ranges[i]
            if min != 10:
                self.log.insert("insert", dt.strftime( '%y-%m-%d %I:%M:%S %p [报错] 检测到近距离障碍物，距离' ))
                self.log.insert("insert", min)
                self.log.insert("insert", "米")
            else:
                self.log.insert("insert", dt.strftime( '%y-%m-%d %I:%M:%S %p [反馈] 机器人向后移动0.15米\n' ))

        else:
            root = Tk()
            root.title('错误')
            root.geometry('300x80')
            lb = Label(root, text='当前没有建图程序在运行', \
                       fg='black', \
                       font=(25), \
                       width=30, \
                       height=2, \
                       relief=SUNKEN)
            lb.pack()
            root.mainloop()

    def go_left(self):
        if self.map == 1:
            self.log.insert("insert", dt.strftime( '%y-%m-%d %I:%M:%S %p [机器人动作] 向左移动\n' ))
            subprocess.Popen('rosrun team_101 go_left', shell=True)
            global ranges
            min = 10
            for i in range(225, 315):
                if len(ranges) > 0 and ranges[i] < 0.5 and ranges[i]<min:
                    min = ranges[i]
            if min != 10:
                self.log.insert("insert", dt.strftime( '%y-%m-%d %I:%M:%S %p [报错] 检测到近距离障碍物，距离' ))
                self.log.insert("insert", min)
                self.log.insert("insert", "米")
            else:
                self.log.insert("insert", dt.strftime( '%y-%m-%d %I:%M:%S %p [反馈] 机器人向左移动0.15米\n' ))

        else:
            root = Tk()
            root.title('错误')
            root.geometry('300x80')
            lb = Label(root, text='当前没有建图程序在运行', \
                       fg='black', \
                       font=(25), \
                       width=30, \
                       height=2, \
                       relief=SUNKEN)
            lb.pack()
            root.mainloop()

    def go_right(self):
        if self.map == 1:
            self.log.insert("insert", dt.strftime( '%y-%m-%d %I:%M:%S %p [机器人动作] 向右移动\n' ))
            subprocess.Popen('rosrun team_101 go_right', shell=True)
            global ranges
            min = 10
            for i in range(45, 135):
                if len(ranges) > 0 and ranges[i] < 0.5 and ranges[i]<min:
                    min = ranges[i]
            if min != 10:
                self.log.insert("insert", dt.strftime( '%y-%m-%d %I:%M:%S %p [报错] 检测到近距离障碍物，距离' ))
                self.log.insert("insert", min)
                self.log.insert("insert", "米")
            else:
                self.log.insert("insert", dt.strftime( '%y-%m-%d %I:%M:%S %p [反馈] 机器人向右移动0.15米\n' ))
        else:
            root = Tk()
            root.title('错误')
            root.geometry('300x80')
            lb = Label(root, text='当前没有建图程序在运行', \
                       fg='black', \
                       font=(25), \
                       width=30, \
                       height=2, \
                       relief=SUNKEN)
            lb.pack()
            root.mainloop()

    def stop(self):
        if self.map == 1:
            self.log.insert("insert", dt.strftime( '%y-%m-%d %I:%M:%S %p [机器人动作] 紧急停止\n' ))
            subprocess.Popen('rosrun team_101 stop', shell=True)
        else:
            root = Tk()
            root.title('错误')
            root.geometry('300x80')
            lb = Label(root, text='当前没有建图程序在运行', \
                       fg='black', \
                       font=(25), \
                       width=30, \
                       height=2, \
                       relief=SUNKEN)
            lb.pack()
            root.mainloop()

    def turn_right(self):
        if self.map == 1:
            self.log.insert("insert", dt.strftime( '%y-%m-%d %I:%M:%S %p [机器人动作] 向右转15度\n' ))
            subprocess.Popen('rosrun team_101 turn_right', shell=True)
        else:
            root = Tk()
            root.title('错误')
            root.geometry('300x80')
            lb = Label(root, text='当前没有建图程序在运行', \
                       fg='black', \
                       font=(25), \
                       width=30, \
                       height=2, \
                       relief=SUNKEN)
            lb.pack()
            root.mainloop()

    def turn_left(self):
        if self.map == 1:
            self.log.insert("insert", dt.strftime( '%y-%m-%d %I:%M:%S %p [机器人动作] 向左转15度\n' ))
            subprocess.Popen('rosrun team_101 turn_left', shell=True)
        else:
            root = Tk()
            root.title('错误')
            root.geometry('300x80')
            lb = Label(root, text='当前没有建图程序在运行', \
                       fg='black', \
                       font=(25), \
                       width=30, \
                       height=2, \
                       relief=SUNKEN)
            lb.pack()
            root.mainloop()
    
    def go_long(self):
        if self.map ==1 :
            self.log.insert("insert", dt.strftime( '%y-%m-%d %I:%M:%S %p [机器人动作] 直走\n' ))
            subprocess.Popen('rosrun team_101 go_long', shell=True)
            global ranges
            min = 10
            for i in range(160, 210):
                if len(ranges) > 0 and ranges[i] < 0.5 and ranges[i]<min:
                    min = ranges[i]
            if min != 10:
                self.log.insert("insert", dt.strftime( '%y-%m-%d %I:%M:%S %p [报错] 检测到近距离障碍物，距离' ))
                self.log.insert("insert", min)
                self.log.insert("insert", "米")

        else:
            root = Tk()
            root.title('错误')
            root.geometry('300x80')
            lb = Label(root, text='当前没有建图程序在运行', \
                       fg='black', \
                       font=(25), \
                       width=30, \
                       height=2, \
                       relief=SUNKEN)
            lb.pack()
            root.mainloop()
