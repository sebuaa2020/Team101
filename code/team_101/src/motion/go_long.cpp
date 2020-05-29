#include <ros/ros.h>
#include <geometry_msgs/Twist.h>
#include <std_msgs/String.h>
#include <iostream>
#include <fstream>   
#include <sensor_msgs/LaserScan.h>
#include <geometry_msgs/Twist.h>
#define go_times 1000000
#define stop_time 1000000

int stop_flag = 0;
std::vector<float> range;

void chatterCallback(const std_msgs::String::ConstPtr& msg)
{
	ROS_INFO("I heard: [%s]", msg->data.c_str());
	stop_flag = 1;
}

void laserCallback(const sensor_msgs::LaserScan::ConstPtr& msg)
{	
	range=msg->ranges;
}

int main(int argc, char** argv) { 

	ros::init(argc, argv, "go_forward"); 
	ros::NodeHandle n;
	ros::Publisher vel_pub = n.advertise<geometry_msgs::Twist>("/cmd_vel", 10);
	ros::Subscriber stop_sub = n.subscribe("chatter", 1, chatterCallback);
	ros::Subscriber laser_sub = n.subscribe("/scan", 1, laserCallback);
	ros::Rate loopRate(10);

    //int times = go_times;
	// int times = 10;

	while(ros::ok()) {
		
		geometry_msgs::Twist vel_cmd;

		ros::spinOnce();

		if (stop_flag == 1) {
			break;
		}
		if (range.size() == 360) {
			int flag = 0;
			for (int i = 160;i < 210;i++) {
				if (range[i] < 0.30) {
					printf("检测到障碍物！");
					flag = 1;
					break;
				}
			}
			if (flag == 1) break;
		}

		vel_cmd.linear.x = 0.2; 
		vel_cmd.linear.y = 0; 
		vel_cmd.linear.z = 0; 

		vel_cmd.angular.x = 0; 
		vel_cmd.angular.y = 0; 
		vel_cmd.angular.z = 0; 
		vel_pub.publish(vel_cmd); 

        	// times--;

		loopRate.sleep();		
	} 

   
    //times = stop_time;
	int times = 10;

	while(ros::ok()&&times>0) {

		geometry_msgs::Twist vel_cmd; 

		vel_cmd.linear.x = 0; 
		vel_cmd.linear.y = 0; 
		vel_cmd.linear.z = 0; 

		vel_cmd.angular.x = 0; 
		vel_cmd.angular.y = 0; 
		vel_cmd.angular.z = 0; 
		vel_pub.publish(vel_cmd); 

        times--;

		loopRate.sleep();
		//ros::spinOnce(); 
	} 


	return 0; 
}
