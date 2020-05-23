import os
class pathCal:
    def __init__(self):
        self.path = ''

    def move(self): #调用ROS包选取导航轨迹
        os.system("gnome-terminal -e 'bash -c \"roslaunch wpb_home_tutorials nav.launch; exec bash\"'")