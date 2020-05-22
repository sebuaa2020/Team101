from map import map
from pathCal import pathCal
import os
class pathAgent:
    def __init__(self, dis):
        self.next_location = dis
        self.m = map()
        self.m.getMap()

    def getpath(self): #调用pathcal类求路径
        p = pathCal(self.next_location)
        p.move()