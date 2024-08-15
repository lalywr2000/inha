#include "ros/ros.h"
#include "sensor_msgs/LaserScan.h"

#include <vector>
#include <cmath>

#define VIEW_ANGLE_DEG 180.0f

ros::Publisher publication_;

sensor_msgs::LaserScan scan_1;
sensor_msgs::LaserScan scan_2;
sensor_msgs::LaserScan fusion_data;

bool update_1 = false;
bool update_2 = false;

std::vector<float> temp;

size_t point_size_1, point_size_2, temp_size;
int idx;

void fusion_pub() {
  temp.resize(0);
  point_size_1 = scan_1.ranges.size();
  point_size_2 = scan_2.ranges.size();

  idx = 0;
  for (float val = 0.0f; val <= VIEW_ANGLE_DEG * 3.14159f / 180.0f; val += scan_1.angle_increment)
  {
    temp.push_back(scan_1.ranges[(idx + (int)(point_size_1 * VIEW_ANGLE_DEG / 720.0f)) % point_size_1]);
    idx++;
  }

  idx = 0;
  for (float val = 0.0f; val <= VIEW_ANGLE_DEG * 3.14159f / 180.0f; val += scan_2.angle_increment)
  {
    temp.push_back(scan_2.ranges[(idx + (int)(point_size_2 * VIEW_ANGLE_DEG / 720.0f)) % point_size_2]);
    idx++;
  }

  fusion_data.ranges.resize(0);
  temp_size = temp.size();

  for (size_t i = 0; i < temp_size; i++)
  {
    fusion_data.ranges.push_back(temp[(temp_size + i - 65) % temp_size]);
  }

  fusion_data.angle_increment = 3.14159f * 2.0f / temp_size;
  fusion_data.header.stamp = ros::Time::now();

  publication_.publish(fusion_data);
  // ROS_INFO("Published!");
}

void topic_callback_1(const sensor_msgs::LaserScan msg) {
  scan_1.ranges = msg.ranges;
  scan_1.angle_increment = msg.angle_increment;
  update_1 = true;

  if (update_1 && update_2) {
    fusion_pub();

    update_1 = false;
    update_2 = false;
  }
}

void topic_callback_2(const sensor_msgs::LaserScan msg) {
  scan_2.ranges = msg.ranges;
  scan_2.angle_increment = msg.angle_increment;
  update_2 = true;

  if (update_1 && update_2) {
    fusion_pub();

    update_1 = false;
    update_2 = false;
  }
}

int main(int argc, char **argv) {
  ros::init(argc, argv, "fusion_node");
  ros::NodeHandle n;
  ros::Subscriber subscription_1 = n.subscribe("/scan_1", 1, topic_callback_1);
  ros::Subscriber subscription_2 = n.subscribe("/scan_2", 1, topic_callback_2);
  publication_ = n.advertise<sensor_msgs::LaserScan>("/fusion", 1);

  fusion_data.header.frame_id = "laser_fusion";
  fusion_data.angle_min = -180.0f;
  fusion_data.angle_max = 180.0f;
  fusion_data.range_min = 0.12f;
  fusion_data.range_max = 10.0f;
  fusion_data.intensities.resize(0);

  ros::spin();

  return 0;
}
