#include "ros/ros.h"
#include "laser_line_extraction/MainWall.h"

#define WALL_DRIVE_DIST 1.1f
#define WALL_DROP_DIST 0.8f

// #define WALL_DIST_NOISE_FACTOR ???
#define INCLINE_ALIGN_NOISE_FACTOR 0.15f

using namespace std;


float distance, incline;


void topic_callback(const laser_line_extraction::MainWall msg) {
  cout << msg.distance << endl;
}


int main(int argc, char **argv) {
  ros::init(argc, argv, "control_node");
  ros::NodeHandle n;

  ros::Subscriber subscription_ = n.subscribe("/main_wall", 1, topic_callback);

  ros::spin();

  return 0;
}


/*
2. control to keep the distance. go find wall to certain direction and make it stop.
3. consider the angle of the wall and make it align to the wall.
4. examine the 4 direction of the wall and follow the wall CCW.
*/