# -*- coding: utf-8 -*-
from tkinter import *
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
nav = pathAgent()
#抓取界面，目前为空
def grab():
    print("This is a dummy precedure")

#建图模块
def build_map():
    m.buildMap()

#建图模块
def finish_build_map():
    if m.built == 1:
        m.saveMap()
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



def destination():
    nav.getpath()

def finish_destination():
    nav.endProcess()

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
    b1 = Button(root, text='退出', command=root.quit)
    b1.place(relx=0.4, rely=0.8, relwidth=0.2, relheight=0.1)
    root.mainloop()


'''
GUI设计
包括主界面, 建立地图界面, 定点巡航界面, 目标抓取界面
'''
finishBM = False
root= Tk()
#root.attributes("-alpha", 0.5)
root['background']='white' #背景颜色
root.title('简单ROS机器人控制程序')
root.geometry('1000x500') # 这里的乘号不是 * ，而是小写英文字母 x

btn1 = Button(root, text='建立地图', command=build_map)
btn1.place(relx=0.1, rely=0.15, relwidth=0.2, relheight=0.1)
btn1['background']='LightCyan' #按钮颜色
btn4 = Button(root, text='停止建图', command=finish_build_map)
btn4.place(relx=0.1, rely=0.35, relwidth=0.2, relheight=0.1)
btn4['background']='LightCyan'
btn2 = Button(root, text='定点巡航', command=destination)
btn2.place(relx=0.4, rely=0.15, relwidth=0.2, relheight=0.1)
btn2['background']='LightCyan'
btn5 = Button(root, text='停止巡航', command=finish_destination)
btn5.place(relx=0.4, rely=0.35, relwidth=0.2, relheight=0.1)
btn5['background']='LightCyan'
btn3 = Button(root, text='目标抓取', command=grab)
btn3.place(relx=0.7, rely=0.15, relwidth=0.2, relheight=0.1)
btn3['background']='LightCyan'
mo = move(0,0,0,m.built)
b1 = Button(root, text='向左转，q键', command=mo.turn_left)
b1.place(relx=0.1, rely=0.55, relwidth=0.2, relheight=0.1)
b1['background']='DarkCyan' #按钮颜色
b2 = Button(root, text='向右转，e键', command=mo.turn_right)
b2.place(relx=0.3, rely=0.55, relwidth=0.2, relheight=0.1)
b2['background']='DarkCyan'
b3 = Button(root, text='向前，w键', command=mo.go_forward)
b3.place(relx=0.5, rely=0.55, relwidth=0.2, relheight=0.1)
b3['background']='DarkCyan'
b4 = Button(root, text='向后，s键', command=mo.go_backward)
b4.place(relx=0.7, rely=0.55, relwidth=0.2, relheight=0.1)
b4['background']='DarkCyan'
b5 = Button(root, text='向前直走', command=mo.go_long)
b5.place(relx=0.1, rely=0.75, relwidth=0.2, relheight=0.1)
b5['background']='DarkCyan'
b6 = Button(root, text='停止，空格键', command=mo.stop)
b6.place(relx=0.7, rely=0.75, relwidth=0.2, relheight=0.1)
b6['background']='DarkCyan'
root.mainloop()
