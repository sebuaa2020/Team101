import rospy
from sensor_msgs.msg import LaserScan
def listener():
    rospy.init_node('get_laser')
    rospy.sleep(2)
    data = rospy.wait_for_message("/scan", LaserScan, timeout=None)
    ranges = data.ranges
    for i in range(160, 210):
        print ranges[i]
   
if __name__ == '__main__':
    listener()
    print "shit"
