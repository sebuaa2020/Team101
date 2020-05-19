from tkinter import *
import os
from PIL import Image, ImageTk
import time
import matplotlib.pyplot as plt
import pylab
import subprocess
import map
x=-1
y=-1

def grab():
    x=-1

def build_map():
    '''
    root = Tk()
    root.title ('建立地图')
    root.geometry('600x500')
    root.mainloop()'''
    os.system("gnome-terminal -e 'bash -c \"roslaunch wpr_simulation wpb_simple.launch; exec bash\"'")
    time.sleep(2)
    os.system("gnome-terminal -e 'bash -c \"roslaunch wpb_home_tutorials gmapping.launch; exec bash\"'")
    time.sleep(2)
    os.system("gnome-terminal -e 'bash -c \"rosrun wpr_simulation keyboard_vel_ctrl; exec bash\"'")
    time.sleep(2)
    os.system("gnome-terminal -e 'bash -c \"rosrun map_server map_saver -f map; exec bash\"'")




def dnq(root1):
    x=-1
    y=-1
    root1.destroy()

def destination():
    path = os.getcwd() + '\maps\map.pgm'
    im = Image.open(path)
    #im.show()
    plt.imshow(im, cmap=plt.get_cmap("gray"))
    pos = plt.ginput(1)
    x=pos[0][0]
    y=pos[0][1]
    if x > 0 and y > 0:
        root = Tk()
        root.title('是否确定选择终点？')
        root.geometry('300x50')
        b = Button(root, text='确定', command=root.destroy)
        b.place(relx=0.1, rely=0.2, relwidth=0.3, relheight=0.7)
        b1 = Button(root, text='退出', command=lambda: dnq(root))
        b1.place(relx=0.6, rely=0.2, relwidth=0.3, relheight=0.7)
        root.mainloop()




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

root= Tk()
root.title('简单ROS机器人控制程序')
root.geometry('1000x500') # 这里的乘号不是 * ，而是小写英文字母 x

btn1 = Button(root, text='建立地图', command=build_map)
btn1.place(relx=0.1, rely=0.4, relwidth=0.2, relheight=0.1)

btn2 = Button(root, text='定点巡航', command=navigation)
btn2.place(relx=0.4, rely=0.4, relwidth=0.2, relheight=0.1)

btn2 = Button(root, text='目标抓取', command=grab)
btn2.place(relx=0.7, rely=0.4, relwidth=0.2, relheight=0.1)
root.mainloop()