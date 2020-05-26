# -*- coding: utf-8 -*-
import os
import subprocess
import os
class move: #基础运动
    '''
    def __init__(self, location, direction, speed):
        self.location = location
        self.direction = direction
        self.speed = speed
    
    def move(self):
        if self.direction == 'go_forward':
            self.go_forward()
        elif self.direction == 'go_backward':
            self.go_backward()
        elif self.direction == 'go_left':
            self.go_left()
        elif self.direction == 'go_right':
            self.go_right()
        elif self.direction == 'turn_left':
            self.turn_left()
        elif self.direction == 'turn_right':
            self.turn_right()
    
    def set_target(self,location, direction):
        self.target = (location,direction)
    '''

    def has_obstruction(self):
        os.system("gnome-terminal -e 'bash -c \"roslaunch wpb_home_bringup lidar_test.launch; exec bash\"'")#启动雷达

    def go_forward(self):
        subprocess.Popen('rosrun team_101 go_forward', shell=True)

    def go_backward(self):
        subprocess.Popen('rosrun team_101 go_backward', shell=True)

    def go_left(self):
        subprocess.Popen('rosrun team_101 go_left', shell=True)

    def go_right(self):
        subprocess.Popen('rosrun team_101 go_right', shell=True)

    def stop(self):
        subprocess.Popen('rosrun team_101 stop', shell=True)

    def turn_right(self):
        subprocess.Popen('rosrun team_101 turn_right', shell=True)

    def turn_left(self):
        subprocess.Popen('rosrun team_101 turn_left', shell=True)
    
    def go_long(self):
        subprocess.Popen('rosrun team_101 go_long', shell=True)
