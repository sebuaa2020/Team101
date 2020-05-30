# -*- coding: utf-8 -*-
from map import Map
from pathCal import pathCal
import os
class pathAgent:
    def __init__(self):
        #self.m = map()
        #self.m.getMap()
        self.m = ''

    def getpath(self): #调用pathcal类求路径
        self.p = pathCal()
        self.p.move()

    def endProcess(self): #中止导航过程
        self.p.endMove()