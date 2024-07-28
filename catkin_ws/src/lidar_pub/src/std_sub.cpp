#include "ros/ros.h"
#include "std_msgs/String.h"

void msgCallback(const std_msgs::String::ConstPtr& msg)
{
  ROS_INFO("Subscribed!");
}

int main(int argc, char **argv)
{
  ros::init(argc, argv, "sub_node");
  ros::NodeHandle n;
  ros::Subscriber sub = n.subscribe("std_msg", 1000, msgCallback);

  ros::spin();

  return 0;
}
