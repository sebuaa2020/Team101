import os
class pathCal:
    path = ''
    def __init__(self,velocity,location):
        self.velocity = velocity
        self.location = location

    def move(self): #调用ROS包选取导航轨迹
        os.system("gnome-terminal -e 'bash -c \"roslaunch wpb_home_tutorials nav.launch; exec bash\"'")