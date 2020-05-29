#include <ros/ros.h>
#include <std_msgs/String.h>
#include <sstream>
#define go_times 1000000
#define stop_time 1000000


int main(int argc, char** argv) { 

	
	ros::init(argc, argv, "stop"); 
	ros::NodeHandle n; 
        ros::Publisher stop_pub = n.advertise<std_msgs::String>("chatter", 10);
	ros::Rate loopRate(10);

	int time = 10;
	while(ros::ok() && time > 0){
		std_msgs::String msgs;
		
		std::stringstream ss;
		ss << "stop";
		msgs.data = ss.str();

		// ROS_INFO("stop");
		stop_pub.publish(msgs);
		time--;

		loopRate.sleep();
		
	}
	return 0;
}
