from map import map
from pathCal import pathCal
import os
class pathAgent:
    def __init__(self):
        self.m = map()
        self.m.getMap()

    def getpath(self): #调用pathcal类求路径
        p = pathCal(self)
        p.move()