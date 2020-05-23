import os
import subprocess
import time

class pathCal:
    def __init__(self):
        self.path = ''

    def move(self): #调用ROS包选取导航轨迹
        subprocess.Popen(['gnome-terminal', '--disable-factory', '-e',
                          'bash  -c \"roslaunch team_101 robot_spawn.launch; exec bash\"'],
                         preexec_fn=os.setpgrp)
        time.sleep(10)
        subprocess.Popen(['gnome-terminal', '--disable-factory', '-e',
                          'bash -c \"roslaunch team_101 navigation.launch; exec bash\"'],
                         preexec_fn=os.setpgrp)

