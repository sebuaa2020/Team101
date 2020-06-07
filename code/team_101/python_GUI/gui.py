# -*- coding: utf-8 -*-
from tkinter import *
import os
from PIL import ImageTk
import time
import matplotlib.pyplot as plt
import pylab
import subprocess
from map import *
from motion import *
from pathAgent import *
import numpy as np
import tkinter
import PIL.Image
import threading
from ExceptionHandler import *


m = Map()
nav = pathAgent()

#多线程记录时间,一定时间杀死程序
def kill(top):
    time.sleep(200)
    if m.built == 0:
        error = Exception(3,0,top)
        error.ExceptionHandler()


#抓取界面，目前为空
def grab():
    print("This is a dummy precedure")

#建图模块
def build_map(top):
    th = threading.Thread(target=kill, args=(top,))
    th.setDaemon(True)  # 守护线程
    th.start()
    m.buildMap()

#建图模块
def finish_build_map():
    if m.built == 1:
        m.saveMap()
        m.built=0
    else:
        end = Toplevel()
        end.title('错误')
        end.geometry('450x200')
        end.resizable(False, False)
        canvas_end = tkinter.Canvas(end, width=450, height=200)
        im_end = get_image('map_error.png', 450, 200)
        canvas_end.create_image(220,100, image=im_end)
        canvas_end.pack()
        end.mainloop()

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
def get_image(filename, width, height):
    im = PIL.Image.open(filename).resize((width,height))
    return ImageTk.PhotoImage(im)

def administrator():#普通用户界面(有建图控制)
    finishBM = False
    root= Tk()
    root.title('简单ROS机器人管理员控制程序')
    root.geometry('800x450') # 这里的乘号不是 * ，而是小写英文字母 x
    root.resizable(False, False)
    
    canvas_root = tkinter.Canvas(root, width=800, height=450)
    im_root = get_image('admin_page.png', 800, 450)
    canvas_root.create_image(402,222, image=im_root)
    canvas_root.pack()

    btn1 = Button(root, relief='flat',font=('等线', 12), fg='#ffffff', text='建立地图', command=lambda :build_map(root))
    btn1.place(relx=0.155, rely=0.145, relwidth=0.18, relheight=0.08)
    btn1['background']='#1794ac' #按钮颜色
    btn4 = Button(root, relief='flat',font=('等线', 12), fg='#ffffff', text='停止建图', command=finish_build_map)
    btn4.place(relx=0.155, rely=0.285, relwidth=0.18, relheight=0.08)
    btn4['background']='#a1d4e2'
    
    btn2 = Button(root, relief='flat',font=('等线', 12), fg='#ffffff', text='开始巡航', command = navigation)#command=destination)
    btn2.place(relx=0.635, rely=0.145, relwidth=0.18, relheight=0.08)
    btn2['background']='#a1d4e2'
    btn5 = Button(root, relief='flat',font=('等线', 12), fg='#ffffff', text='停止巡航', command=finish_destination)
    btn5.place(relx=0.635, rely=0.285, relwidth=0.18, relheight=0.08)
    btn5['background']='#1794ac'
    
    btn3 = Button(root, relief='flat',font=('等线', 12), fg='#ffffff', text='目标抓取', command=grab)
    btn3.place(relx=0.155, rely=0.705, relwidth=0.18, relheight=0.08)
    btn3['background']='#a1d4e2'
    
    mo = move(0,0,0,m.built)
    imgl = get_image('left.png',40,40)  #left
    b1 = Button(root, relief='flat', image=imgl, command=mo.turn_left)
    b1.place(relx=0.628, rely=0.695)
    
    imgr = get_image('right.png',40,40) #right
    b2 = Button(root, relief='flat', image=imgr, command=mo.turn_right)
    b2.place(relx=0.762, rely=0.695)
    
    imgu = get_image('up.png',40,40) #up
    b3 = Button(root, relief='flat', image=imgu, command=mo.go_forward)
    b3.place(relx=0.695, rely=0.585)
    
    imgd = get_image('down.png',40,40) #down
    b4 = Button(root, relief='flat', image=imgd, command=mo.go_backward)
    b4.place(relx=0.695, rely=0.815)
    
    imgk = get_image('keep.png',40,40) #keep up
    b5 = Button(root, relief='flat', image=imgk, command=mo.go_long)
    b5.place(relx=0.762, rely=0.585)

    imgs = get_image('stop.png',40,40) #stop
    b6 = Button(root, relief='flat', image=imgs, command=mo.stop)
    b6.place(relx=0.695, rely=0.695)
    
    root.mainloop()

def user(): #普通用户界面(没有建图控制)
    root= Tk()
    root.title('简单ROS机器人用户控制程序')
    root.geometry('800x450') # 这里的乘号不是 * ，而是小写英文字母 x
    root.resizable(False, False)
    
    canvas_root = tkinter.Canvas(root, width=800, height=450)
    im_root = get_image('user_page.png', 800, 450)
    canvas_root.create_image(402,222, image=im_root)
    canvas_root.pack()
    
    btn2 = Button(root, relief='flat',font=('等线', 12), fg='#ffffff', text='开始巡航', command = navigation)#command=destination)
    btn2.place(relx=0.385, rely=0.155, relwidth=0.18, relheight=0.08)
    btn2['background']='#1794ac'
    btn5 = Button(root, relief='flat',font=('等线', 12), fg='#ffffff', text='停止巡航', command=finish_destination)
    btn5.place(relx=0.385, rely=0.285, relwidth=0.18, relheight=0.08)
    btn5['background']='#a1d4e2'
    
    btn3 = Button(root, relief='flat',font=('等线', 12), fg='#ffffff', text='目标抓取', command=grab)
    btn3.place(relx=0.155, rely=0.705, relwidth=0.18, relheight=0.08)
    btn3['background']='#a1d4e2'
    
    mo = move(0,0,0,m.built)
    imgl = get_image('left.png',40,40)  #left
    b1 = Button(root, relief='flat', image=imgl, command=mo.turn_left)
    b1.place(relx=0.588, rely=0.705)
    
    imgr = get_image('right.png',40,40) #right
    b2 = Button(root, relief='flat', image=imgr, command=mo.turn_right)
    b2.place(relx=0.722, rely=0.705)
    
    imgu = get_image('up.png',40,40) #up
    b3 = Button(root, relief='flat', image=imgu, command=mo.go_forward)
    b3.place(relx=0.655, rely=0.585)
    
    imgd = get_image('down.png',40,40) #down
    b4 = Button(root, relief='flat', image=imgd, command=mo.go_backward)
    b4.place(relx=0.655, rely=0.815)
    
    imgk = get_image('keep.png',40,40) #keep up
    b5 = Button(root, relief='flat', image=imgk, command=mo.go_long)
    b5.place(relx=0.722, rely=0.585)

    imgs = get_image('stop.png',40,40) #stop
    b6 = Button(root, relief='flat', image=imgs, command=mo.stop)
    b6.place(relx=0.655, rely=0.705)
    root.mainloop()


def login(E1, E2, top):
    username = E1.get()
    password = E2.get()
    arr = np.load("../database.npy")#读取数据库
    matched  = False
    for i in arr:
        print(i[0],i[1],i[2])
        if i[0] == username:#匹配用户名
            if i[1] == password:#匹配密码
                matched = True
                if i[2] == '1':  # 是管理员
                    top.destroy()
                    administrator()
                    break
                else: #普通用户
                    top.destroy()
                    user()

                    break
    if matched == False: #未匹配到用户名或密码
        root = Toplevel()
        root.title('登录错误')
        root.geometry('450x200')
        root.resizable(False, False)
        canvas_root = tkinter.Canvas(root, width=450, height=200)
        im_root = get_image('login_error.png', 450, 200)
        canvas_root.create_image(220,100, image=im_root)
        canvas_root.pack()
        root.mainloop()


def signin(E1,E2,top):
    username = E1.get()
    password = E2.get()
    arr = np.load("../database.npy")#读取数据库
    arr = np.append(arr,[[username,password,'2']],axis=0)#加入数据库,注意不能随意添加管理员用户,因此新注册用户只能是普通用户
    np.save("../database.npy",arr)#保存数据库
    
    root = Toplevel()
    root.title('注册成功')
    root.geometry('450x200')
    root.resizable(False, False)
    canvas_root = tkinter.Canvas(root, width=450, height=200)
    im_root = get_image('signin.png', 450, 200)
    canvas_root.create_image(220,100, image=im_root)
    canvas_root.pack()
    root.mainloop()



top = Tk()
top.geometry('800x450')
top.title('简单ROS机器人登录')
top.resizable(False, False)

canvas_top = tkinter.Canvas(top, width=800, height=450)
im_top = get_image('login.png', 800, 450)
canvas_top.create_image(402,220, image=im_top)
canvas_top.pack()

E1 = Entry(top, bd=5) #读入用户名
E1.place(relx=0.46, rely=0.40,  relwidth=0.2, relheight=0.07)

password = StringVar()  #读入密码并且不显示密码
E2 = Entry(top, bd=5,textvariable=password,show='*')
E2.place(relx=0.46, rely=0.51, relwidth=0.2, relheight=0.07)
#登录
b1 = Button(top, text='登   录',relief='flat',font=('等线', 14), fg='#ffffff', command=lambda :login(E1, E2, top))
b1.place(relx=0.325, rely=0.65, relwidth=0.13, relheight=0.07)
b1['background']='#a1d4e2'
#注册
b2 = Button(top, text='注   册',relief='flat',font=('等线', 14), fg='#ffffff', command=lambda :signin(E1, E2, top))
b2.place(relx=0.525, rely=0.65, relwidth=0.13, relheight=0.07)
b2['background']='#1794ac'
top.mainloop()