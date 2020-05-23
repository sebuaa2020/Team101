# -*- coding: utf-8 -*-
from Tkinter import *
import os
from PIL import Image, ImageTk
import time
import matplotlib.pyplot as plt
import pylab
import subprocess
from map import *
from motion import *
from pathAgent import *

#标记
x=-1
y=-1

user = 1 #标记是否是管理员
m = Map()
#抓取界面，目前为空
def grab():
    print("This is a dummy precedure")

#建图模块
def build_map():
    if user == 1 : #是管理员
        m.buildMap()

#建图模块
def finish_build_map():
    m.saveMap()


def destination():
    nav = pathAgent()
    nav.getpath()

    

#导航模块
def navigation():
    root = Tk()
    root.title('定点巡航')
    root.geometry('600x500')
    lb = Label(root, text='请选择目标终点', \
               fg='red', \
               font=(32), \
               width=20, \
               height=2, \
               relief=SUNKEN)
    lb.pack()
    btn3 = Button(root, text='选择终点', command=destination)
    btn3.place(relx=0.4, rely=0.4, relwidth=0.2, relheight=0.1)
    b = Button(root, text='确定', command=root.destroy)
    b.place(relx=0.1, rely=0.8, relwidth=0.2, relheight=0.1)
    b1 = Button(root, text='退出', command=lambda: dnq(root))
    b1.place(relx=0.7, rely=0.8, relwidth=0.2, relheight=0.1)
    root.mainloop()


'''
GUI设计
包括主界面, 建立地图界面, 定点巡航界面, 目标抓取界面
'''
finishBM = False
root= Tk()
root.title('简单ROS机器人控制程序')
root.geometry('1000x500') # 这里的乘号不是 * ，而是小写英文字母 x

btn1 = Button(root, text='建立地图', command=build_map)
btn1.place(relx=0.1, rely=0.4, relwidth=0.2, relheight=0.1)

btn4 = Button(root, text='停止建图', command=finish_build_map)
btn4.place(relx=0.1, rely=0.6, relwidth=0.2, relheight=0.1)

btn2 = Button(root, text='定点巡航', command=navigation)
btn2.place(relx=0.4, rely=0.4, relwidth=0.2, relheight=0.1)

btn3 = Button(root, text='目标抓取', command=grab)
btn3.place(relx=0.7, rely=0.4, relwidth=0.2, relheight=0.1)

mo = move()
b1 = Button(root, text='向左转', command=mo.turn_left)
b1.place(relx=0.1, rely=0.8, relwidth=0.2, relheight=0.1)
b2 = Button(root, text='向右转', command=mo.turn_right)
b2.place(relx=0.3, rely=0.8, relwidth=0.2, relheight=0.1)
b3 = Button(root, text='向前', command=mo.go_forward)
b3.place(relx=0.5, rely=0.8, relwidth=0.2, relheight=0.1)
b4 = Button(root, text='向后', command=mo.go_backward)
b4.place(relx=0.7, rely=0.8, relwidth=0.2, relheight=0.1)

root.mainloop()