#include "ros/ros.h"
#include "laser_line_extraction/LineSegment.h"
#include "laser_line_extraction/LineSegmentList.h"
#include <geometry_msgs/Point.h>
#include <visualization_msgs/Marker.h>
#include <visualization_msgs/MarkerArray.h>

#include <cmath>
#include <vector>
#include <algorithm>

using namespace std;

namespace Color {
  const vector<float> RED     = {1.0f, 0.0f, 0.0f, 1.0f};
  const vector<float> GREEN   = {0.0f, 1.0f, 0.0f, 1.0f};
  const vector<float> BLUE    = {0.0f, 0.0f, 1.0f, 1.0f};
  const vector<float> YELLOW  = {1.0f, 1.0f, 0.0f, 1.0f};
  const vector<float> ORANGE  = {1.0f, 0.5f, 0.0f, 1.0f};
  const vector<float> WHITE   = {1.0f, 1.0f, 1.0f, 1.0f};
  const vector<float> GRAY    = {0.5f, 0.5f, 0.5f, 1.0f};
}


vector<vector<float>> line_info;
float x_start, y_start, x_end, y_end;

visualization_msgs::MarkerArray marker_array;


void visualizeLine(vector<float> start_point,
                   vector<float> end_point,
                   vector<float> rgba,
                   float scale) {
  visualization_msgs::Marker marker;
	geometry_msgs::Point point;

	marker.header.frame_id = "map";
  marker.header.stamp = ros::Time::now();
  marker.id = rand();
  marker.type = visualization_msgs::Marker::LINE_STRIP;
  marker.action = visualization_msgs::Marker::ADD;
	marker.lifetime = ros::Duration(0.1);

  marker.pose.position.x = 0.0f;
  marker.pose.position.y = 0.0f;
	marker.pose.position.z = 0.0f;
	marker.pose.orientation.x = 0.0f;
	marker.pose.orientation.y = 0.0f;
	marker.pose.orientation.z = 0.0f;
	marker.pose.orientation.w = 1.0f;

  point.x = start_point[0];
  point.y = start_point[1];
  marker.points.push_back(point);
  point.x = end_point[0];
  point.y = end_point[1];
  marker.points.push_back(point);

  marker.color.r = rgba[0];
  marker.color.g = rgba[1];
  marker.color.b = rgba[2];
  marker.color.a = rgba[3];

  marker.scale.x = scale;

  marker_array.markers.push_back(marker);
}

void visualizePoint(vector<float> point,
                    vector<float> rgba,
                    float scale) {
  visualization_msgs::Marker marker;

  marker.header.frame_id = "map";
  marker.header.stamp = ros::Time::now();
  marker.id = rand();
  marker.type = visualization_msgs::Marker::SPHERE;
  marker.action = visualization_msgs::Marker::ADD;
  marker.lifetime = ros::Duration(0.1);

  marker.pose.position.x = point[0];
  marker.pose.position.y = point[1];
  marker.pose.position.z = 0.0f;
  marker.pose.orientation.x = 0.0f;
  marker.pose.orientation.y = 0.0f;
  marker.pose.orientation.z = 0.0f;
  marker.pose.orientation.w = 1.0f;

  marker.color.r = rgba[0];
  marker.color.g = rgba[1];
  marker.color.b = rgba[2];
  marker.color.a = rgba[3];

  marker.scale.x = scale;
  marker.scale.y = scale;
  marker.scale.z = scale;

  marker_array.markers.push_back(marker);
}

float getLineDist(float x1, float y1, float x2, float y2) {
  float incline = (y2 - y1) / (x2 - x1);
  float intercept = y1 - incline * x1;

  return abs(intercept) / sqrt(incline * incline + 1.0f);
}

void msgCallback(const laser_line_extraction::LineSegmentList msg) {
  // ROS_INFO("Subscribed!");

  line_info.clear();
  marker_array.markers.clear();

  visualizePoint({0.0f, 0.0f}, Color::ORANGE, 0.3f);

  if (msg.line_segments.size() > 0) {
    for (int i = 0; i < msg.line_segments.size(); i++) {
      x_start = msg.line_segments[i].start[0];
      y_start = msg.line_segments[i].start[1];
      x_end = msg.line_segments[i].end[0];
      y_end = msg.line_segments[i].end[1];

      line_info.push_back({getLineDist(x_start, y_start, x_end, y_end), x_start, y_start, x_end, y_end});
    }

    sort(line_info.begin(), line_info.end(), [](const vector<float>& a, const vector<float>& b) { return a[0] < b[0]; });

    for (int i = 0; i < line_info.size(); i++) {
      visualizeLine({line_info[i][0], line_info[i][1]}, {line_info[i][2], line_info[i][3]}, Color::WHITE, 0.1f);
    }
  }

  pub.publish(marker_array);
  // ROS_INFO("Published!");
}


int main(int argc, char **argv) {
  ros::init(argc, argv, "processing_node");
  ros::NodeHandle n;

  ros::Subscriber sub = n.subscribe("/line_segments", 1, msgCallback);
  ros::Publisher pub = n.advertise<visualization_msgs::MarkerArray>("/vis", 1);

  ros::spin();

  return 0;
}

/*
1. get nearest wall and distance of it.
2. select appropriate distance and make control code to keep the distance.
3. consider the angle of the wall and make it align to the wall.
4. examine the 4 direction of the wall and follow the wall CCW.
*/
