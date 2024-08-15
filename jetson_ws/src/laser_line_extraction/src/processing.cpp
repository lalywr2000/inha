#include "ros/ros.h"
#include "laser_line_extraction/LineSegment.h"
#include "laser_line_extraction/LineSegmentList.h"

#include <vector>

void msgCallback(const laser_line_extraction::LineSegmentList msg) {
  std::cout << msg.size() << std::endl;
  // ROS_INFO("Subscribed!");
}

int main(int argc, char **argv) {
  ros::init(argc, argv, "processing_node");
  ros::NodeHandle n;

  ros::Subscriber sub = n.subscribe("/line_segments", 1, msgCallback);

  ros::spin();

  return 0;
}



// ============
// int main(int argc, char **argv)
// {
//   ros::init(argc, argv, "pub_node");
//   ros::NodeHandle n;
//   ros::Publisher pub = n.advertise<std_msgs::String>("std_msg", 1000);
//   ros::Rate loop_rate(10);

//   while (ros::ok())
//   {
//     std_msgs::String msg;
//     msg.data = "hello world";

//     pub.publish(msg);
//     ROS_INFO("Published!");

//     ros::spinOnce();
//     loop_rate.sleep();
//   }

//   return 0;
// }
