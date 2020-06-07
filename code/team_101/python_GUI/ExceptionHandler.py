# -*- coding: utf-8 -*-
from motion import *
import time
import os
from tkinter import *
import sys
class Exception:
    def __init__(self,type,current,root):
        self.ExceptionType = type #异常类型
        self.current = current #记录当前行为
        self.root = root #
    '''
    Different types of defects:
    0 : 停止机器人[使用场景: 撞到物体时等]
    1 : 停止机器人10s, 再次检测是否适宜移动.是则恢复原事件,否则停止机器人[使用场景: 激光雷达监测到障碍物时]
    2 : 机械臂归位[使用场景: 抓取失败时]
    3 : 重启程序[使用场景: gazebo软件异常]
    '''
    def ExceptionHandler(self):
        if self.ExceptionType == 0 :
            m = move(0,'stop')
            m.stop()
        elif self.ExceptionType == 1 :
            m = move(0,'stop')
            m.stop()
            time.sleep(10)
            m_resume = move(0.2,self.current)
            #m_resume.move
        elif self.ExceptionType == 2 :
            print("action to be complete in grab")
        elif self.ExceptionType == 3 :
            root = Tk()
            root.title('错误')
            root.geometry('500x150')
            lb = Label(root, text='检测到长时间未建立地图，若无法建图,请重启程序', \
                       fg='black', \
                       font=(24), \
                       width=50, \
                       height=2, \
                       relief=SUNKEN)
            lb.pack()
            root.mainloop()
