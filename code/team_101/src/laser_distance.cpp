#include "ros/ros.h"
#include <iostream>
#include <fstream>   
#include <sensor_msgs/LaserScan.h>

void laserCallback(const sensor_msgs::LaserScan::ConstPtr& msg)
{
    std::vector<float> ranges=msg->ranges;
    std::cout<< ranges.size()<<" ";

    std::cout<< msg->header.stamp<<" ";
    std::cout<< msg->header.frame_id<<" ";
    std::cout<< msg->angle_min<<" ";
    std::cout<< msg->angle_max<<" ";
	std::cout<< msg->angle_increment<<" ";
	std::cout<< msg->time_increment<<" ";
	std::cout<< "dis_ranges:"<<  msg->range_min<<" ";
    std::cout<< "dis_ranges:"<<  ranges[180]<<" fuck ";
	std::cout<< msg->range_max<<" ";
    std::cout<<"\n";
}
int main(int argc, char **argv)
{

    ros::init(argc, argv, "laser_distance");
    ros::NodeHandle nh;
    ros::Subscriber sub = nh.subscribe("/scan", 1, laserCallback);
    ros::spin();

    return 0;
}
