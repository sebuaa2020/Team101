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
import numpy as np


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

def administrator():
    finishBM = False
    root= Tk()
    #root.attributes("-alpha", 0.5)
    root['background']='white' #背景颜色
    root.title('简单ROS机器人管理员控制程序')
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

def user():
    root= Tk()
    root.title('简单ROS机器人用户控制程序')
    root.geometry('1000x500') # 这里的乘号不是 * ，而是小写英文字母 x
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


def login(E1, E2, top):
    username = E1.get()
    password = E2.get()
    arr = np.load("../database.npy")
    print(username,password)
    matched  = False
    for i in arr:
        print(i[0],i[1],i[2])
        if i[0] == username:
            if i[1] == password:
                matched = True
                if i[2] == '1':  # 是管理员
                    top.destroy()
                    administrator()
                    break
                else:
                    top.destroy()
                    user()

                    break
    if matched == False:
        root = Tk()
        root.title('错误')
        root.geometry('300x80')
        lb = Label(root, text='错误密码或用户名', \
                   fg='black', \
                   font=(25), \
                   width=30, \
                   height=2, \
                   relief=SUNKEN)
        lb.pack()
        root.mainloop()


def signin(E1,E2,top):
    username = E1.get()
    password = E2.get()
    arr = np.load("../database.npy")
    arr = np.append(arr,[[username,password,'2']],axis=0)
    np.save("../database.npy",arr)

top = Tk()
top.geometry('1000x500')
top.title('简单ROS机器人登录')
L1 = Label(top, text="用户名")
L1.place(relx=0.25, rely=0.3, relwidth=0.15, relheight=0.07)

E1 = Entry(top, bd=5)
E1.place(relx=0.40, rely=0.3, relwidth=0.2, relheight=0.07)
L2 = Label(top, text="密码")
L2.place(relx=0.25, rely=0.4, relwidth=0.15, relheight=0.07)
password = StringVar()
E2 = Entry(top, bd=5,textvariable=password,show='*')

E2.place(relx=0.4, rely=0.4, relwidth=0.2, relheight=0.07)

b1 = Button(top, text='登录', command=lambda :login(E1, E2, top))
b1.place(relx=0.35, rely=0.6, relwidth=0.1, relheight=0.07)

b2 = Button(top, text='注册', command=lambda :signin(E1, E2, top))
b2.place(relx=0.55, rely=0.6, relwidth=0.1, relheight=0.07)
top.mainloop()