# -*- coding: utf-8 -*-

import subprocess
import os
from ExceptionHandler import *
from Tkinter import *
class move: #基础运动

    def __init__(self, location, direction, speed,map):
        self.location = location
        self.direction = direction
        self.speed = speed
        self.map = map



    def has_obstruction(self):
        os.system("gnome-terminal -e 'bash -c \"roslaunch wpb_home_bringup lidar_test.launch; exec bash\"'")#启动雷达

    def obstruction_excepetion(self):
        error = Exception(1,self.direction)
        error.ExceptionHandler()

    def go_forward(self):
        if map == 1:
            subprocess.Popen('rosrun team_101 go_forward', shell=True)
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
        if map == 1:
            subprocess.Popen('rosrun team_101 go_backward', shell=True)
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
        if map == 1:
            subprocess.Popen('rosrun team_101 go_left', shell=True)
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
        if map == 1:
            subprocess.Popen('rosrun team_101 go_right', shell=True)
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
        if map == 1:
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
        if map == 1:
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
        if map == 1:
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
        if map ==1 :
            subprocess.Popen('rosrun team_101 go_long', shell=True)
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
