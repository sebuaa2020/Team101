#include <ros/ros.h>
#include <iostream>
#include <fstream>   
#include <sensor_msgs/LaserScan.h>
#include <geometry_msgs/Twist.h>
#define go_times 1000000
#define stop_time 1000000
std::vector<float> ranges;

void laserCallback(const sensor_msgs::LaserScan::ConstPtr& msg)
{
	ranges=msg->ranges;
}

int main(int argc, char** argv) { 


	ros::init(argc, argv, "go_forward"); 
	ros::NodeHandle n; 
	ros::Publisher vel_pub = n.advertise<geometry_msgs::Twist>("/cmd_vel", 10);
	ros::Rate loopRate(10);
    ros::NodeHandle nh;
    ros::Subscriber sub = nh.subscribe("/scan", 1, laserCallback);

    //int times = go_times;
	int times = 10;

	while(ros::ok()&&times>0) {
		ros::spinOnce();
		geometry_msgs::Twist vel_cmd; 
		
		if (ranges.size() == 360) {
			int flag = 0;
			for (int i = 45;i < 135;i++) {
				if (ranges[i] < 0.30) {
					printf("检测到障碍物！");
					flag = 1;
					break;
				}
			}
			if (flag == 1) break;
		}
		
		vel_cmd.linear.x = 0; 
		vel_cmd.linear.y = -0.2; 
		vel_cmd.linear.z = 0; 

		vel_cmd.angular.x = 0; 
		vel_cmd.angular.y = 0; 
		vel_cmd.angular.z = 0; 
		vel_pub.publish(vel_cmd); 
        times--;

		loopRate.sleep();
		// 
	} 
   
    //times = stop_time;
	times = 10;

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