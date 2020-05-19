import os
class move :

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