#include "ros/ros.h"
#include "std_msgs/String.h"

int main(int argc, char **argv)
{
  ros::init(argc, argv, "pub_node");
  ros::NodeHandle n;
  ros::Publisher pub = n.advertise<std_msgs::String>("std_msg", 1000);
  ros::Rate loop_rate(10);

  while (ros::ok())
  {
    std_msgs::String msg;
    msg.data = "hello world";

    pub.publish(msg);
    ROS_INFO("Published!");

    ros::spinOnce();
    loop_rate.sleep();
  }

  return 0;
}
