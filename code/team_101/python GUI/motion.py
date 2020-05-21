import os
import subprocess

class move :
    
    def go_forward(self):
        subprocess.Popen('rosrun team_101 go_forward',shell=True)

    def go_backward(self):
        subprocess.Popen('rosrun team_101 go_backward',shell=True)

    def go_left(self):
        subprocess.Popen('rosrun team_101 go_left',shell=True)

    def go_right(self):
        subprocess.Popen('rosrun team_101 go_right',shell=True)

    def stop(self):
        subprocess.Popen('rosrun team_101 go_stop',shell=True)

    def turn_right(self):
        subprocess.Popen('rosrun team_101 turn_right',shell=True)

    def turn_left(self):
        subprocess.Popen('rosrun team_101 turn_left',shell=True)
   
