#include "ros/ros.h"
#include "laser_line_extraction/LineSegment.h"
#include "laser_line_extraction/LineSegmentList.h"

#include <cmath>
#include <vector>
#include <algorithm>

using namespace std;

vector<vector<float>> line_info;
float x_start, y_start, x_end, y_end;

float getDist(float x1, float y1, float x2, float y2) {
  return sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2));
}

void msgCallback(const laser_line_extraction::LineSegmentList msg) {
  // ROS_INFO("Subscribed!");

  line_info.clear();

  if (msg.line_segments.size() > 0) {
    for (int i = 0; i < msg.line_segments.size(); i++) {
      x_start = msg.line_segments[i].start[0];
      y_start = msg.line_segments[i].start[1];
      x_end = msg.line_segments[i].end[0];
      y_end = msg.line_segments[i].end[1];

      line_info.push_back({getDist(x_start, y_start, x_end, y_end), x_start, y_start, x_end, y_end});
    }

    sort(line_info.begin(), line_info.end(), [](const vector<float>& a, const vector<float>& b) { return a[0] < b[0]; });

    for (int i = 1; i < 5; i++) {
      cout << line_info[0][i] << endl;
      if (i == 2) {
        cout << "---" << endl;
      }
    }
    cout << "===============" << endl;
  }



  // pub.publish(msg);
  // ROS_INFO("Published!");
}

int main(int argc, char **argv) {
  ros::init(argc, argv, "processing_node");
  ros::NodeHandle n;

  ros::Subscriber sub = n.subscribe("/line_segments", 1, msgCallback);
  // ros::Publisher pub = n.advertise<std_msgs::String>("std_msg", 1000);

  ros::spin();

  return 0;
}



/*
1. get nearest wall and distance of it.
2. select appropriate distance and make control code to keep the distance.
3. consider the angle of the wall and make it align to the wall.
4. examine the 4 direction of the wall and follow the wall CCW.
*/