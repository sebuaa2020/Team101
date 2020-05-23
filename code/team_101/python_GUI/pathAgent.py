# -*- coding: utf-8 -*-
from map import Map
from pathCal import pathCal
import os
class pathAgent:
    def __init__(self):
        self.m = map()
        self.m.getMap()

    def getpath(self): #调用pathcal类求路径
        p = pathCal()
        p.move()