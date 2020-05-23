import os
import subprocess
import os
class move : #基础运动
    def __init__(self,speed,direction):
        self.speed = speed
        self.direction = direction

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


    def has_obstruction(self):
        os.system("gnome-terminal -e 'bash -c \"roslaunch wpb_home_bringup lidar_test.launch; exec bash\"'")#启动雷达

    def go_forward(self):
        os.system("gnome-terminal -e 'bash -c \"rosrun move go_forward; exec bash\"'")

    def go_backward(self):
        os.system("gnome-terminal -e 'bash -c \"rosrun move go_backward; exec bash\"'")

    def go_left(self):
        os.system("gnome-terminal -e 'bash -c \"rosrun move go_left; exec bash\"'")

    def go_right(self):
        os.system("gnome-terminal -e 'bash -c \"rosrun move go_right; exec bash\"'")

    def stop(self):
        os.system("gnome-terminal -e 'bash -c \"rosrun move stop; exec bash\"'")

    def turn_right(self):
        os.system("gnome-terminal -e 'bash -c \"rosrun move turn_right; exec bash\"'")

    def turn_left(self):
        os.system("gnome-terminal -e 'bash -c \"rosrun move go_left; exec bash\"'")
