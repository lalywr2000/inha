#include "ros/ros.h"
#include "sensor_msgs/LaserScan.h"
#include "src/CYdLidar.h"

#include <string>
#include <vector>

std::string str_optval;
int int_optval;
float float_optval;
bool bool_optval;

CYdLidar laser;
LaserScan scan;

sensor_msgs::LaserScan msg;

std::size_t point_size;

int main(int argc, char **argv) {
  ros::init(argc, argv, "lidar_pub_1_node");
  ros::NodeHandle n;
  ros::Publisher pub = n.advertise<sensor_msgs::LaserScan>("scan_1", 1);
  ros::Rate loop_rate(15);

  str_optval = "/dev/lidar_1";
  laser.setlidaropt(LidarPropSerialPort, str_optval.c_str(), str_optval.size());
  int_optval = 128000;
  laser.setlidaropt(LidarPropSerialBaudrate, &int_optval, sizeof(int));
  int_optval = TYPE_TRIANGLE;
  laser.setlidaropt(LidarPropLidarType, &int_optval, sizeof(int));
  int_optval = YDLIDAR_TYPE_SERIAL;
  laser.setlidaropt(LidarPropDeviceType, &int_optval, sizeof(int));
  float_optval = 10.0f;
  laser.setlidaropt(LidarPropScanFrequency, &float_optval, sizeof(float));
  int_optval = 5;
  laser.setlidaropt(LidarPropSampleRate, &int_optval, sizeof(int));
  bool_optval = true;
  laser.setlidaropt(LidarPropSingleChannel, &bool_optval, sizeof(bool));
  float_optval = 180.0f;
  laser.setlidaropt(LidarPropMaxAngle, &float_optval, sizeof(float));
  float_optval = -180.0f;
  laser.setlidaropt(LidarPropMinAngle, &float_optval, sizeof(float));
  float_optval = 10.0f;
  laser.setlidaropt(LidarPropMaxRange, &float_optval, sizeof(float));
  float_optval = 0.12f;
  laser.setlidaropt(LidarPropMinRange, &float_optval, sizeof(float));
  bool_optval = false;
  laser.setlidaropt(LidarPropIntenstiy, &bool_optval, sizeof(bool));

  laser.initialize();
  laser.turnOn();

  if(laser.doProcessSimple(scan)) {
    msg.header.frame_id = "laser_1";
    msg.angle_min = scan.config.min_angle;
    msg.angle_max = scan.config.max_angle;
    msg.range_min = scan.config.min_range;
    msg.range_max = scan.config.max_range;
    msg.intensities.resize(0);
  }

  while (ros::ok()) {
    if(laser.doProcessSimple(scan)) {
      msg.header.stamp = ros::Time::now();
      msg.angle_increment = scan.config.angle_increment;
      msg.time_increment = scan.config.time_increment;
      msg.scan_time = scan.config.scan_time;

      point_size = scan.points.size();
      msg.ranges.resize(point_size);
      for(size_t i = 0; i < point_size; i++)
      {
        msg.ranges[i] = scan.points[(point_size - i - 1 + 30) % point_size].range;  // Change Orientation
      }

      pub.publish(msg);
      // ROS_INFO("Published!");
    }

    ros::spinOnce();
    loop_rate.sleep();
  }

  laser.turnOff();
  laser.disconnecting();

  return 0;
}
