#include "ros/ros.h"
#include "laser_line_extraction/LineSegment.h"
#include "laser_line_extraction/LineSegmentList.h"
#include <geometry_msgs/Point.h>
#include <visualization_msgs/Marker.h>
#include <visualization_msgs/MarkerArray.h>

#include <cmath>
#include <vector>
#include <algorithm>

#define RANGE_OF_INTEREST 5.0f
#define MIN_WALL_LEN 1.0f
#define DRIVE_WALL_DIST 1.3f

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


ros::Publisher visualize_;

vector<vector<float>> line_info;
visualization_msgs::MarkerArray marker_array;

float x_start_temp, y_start_temp, x_end_temp, y_end_temp;
float x_start, y_start, x_end, y_end;
float dist, len;

bool update_1 = false;
bool update_2 = false;


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

float getDist(float x1, float y1, float x2, float y2) {
  return sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2));
}

float getLineDist(float x1, float y1, float x2, float y2) {
  float incline = (y2 - y1) / (x2 - x1);
  float intercept = y1 - incline * x1;

  return abs(intercept) / sqrt(incline * incline + 1.0f);
}

void processing() {
  if (line_info.size() > 0) {
    sort(line_info.begin(), line_info.end(), [](const vector<float>& a, const vector<float>& b) { return a[0] < b[0]; });

    cout << "Nearest wall dist: " << line_info[0][0] << endl;

    // if (line_info[0][0] > DRIVE_WALL_DIST) {
    //   // action
    // } else {
    //   // action
    // }
    // make situation and decision here !!! -> publish ctrl topic !!!
  }

  // if no wall is detected situation !!!
}

void visualize() {
  visualizeLine({0.25f, -0.35f}, {0.25f, 0.35f}, Color::WHITE, 0.05f);
  visualizeLine({0.25f, 0.35f}, {-0.25f, 0.35f}, Color::WHITE, 0.05f);
  visualizeLine({-0.25f, 0.35f}, {-0.25f, -0.35f}, Color::WHITE, 0.05f);
  visualizeLine({-0.25f, -0.35f}, {0.25f, -0.35f}, Color::WHITE, 0.05f);

  visualizeLine({0.21f - 0.0125f, -0.45f}, {0.25f + 0.0125f, -0.45f}, Color::GRAY, 0.1f);
  visualizeLine({0.21f - 0.0125f, 0.45f}, {0.25f + 0.0125f, 0.45f}, Color::GRAY, 0.1f);
  visualizeLine({-0.21f - 0.0125f, 0.45f}, {-0.25f + 0.0125f, 0.45f}, Color::GRAY, 0.1f);
  visualizeLine({-0.21f - 0.0125f, -0.45f}, {-0.25f + 0.0125f, -0.45f}, Color::GRAY, 0.1f);

  visualizePoint({0.0f, -0.415f}, Color::ORANGE, 0.07f);
  visualizePoint({0.0f, 0.415f}, Color::ORANGE, 0.07f);

  if (line_info.size() > 0) {
    for (int i = 0; i < line_info.size(); i++) {
      if (i == 0) {
        visualizeLine({line_info[i][1], line_info[i][2]}, {line_info[i][3], line_info[i][4]}, Color::WHITE, 0.1f);
        visualizeLine({line_info[i][1], line_info[i][2]}, {line_info[i][3], line_info[i][4]}, Color::RED, 0.5f);
      } else {
        visualizeLine({line_info[i][1], line_info[i][2]}, {line_info[i][3], line_info[i][4]}, Color::WHITE, 0.1f);
      }
    }
  }

  visualize_.publish(marker_array);

  line_info.clear();
  marker_array.markers.clear();
}

void topic_callback_1(const laser_line_extraction::LineSegmentList msg) {
  if (update_1) return;

  if (msg.line_segments.size() > 0) {
    for (int i = 0; i < msg.line_segments.size(); i++) {
      x_start_temp = msg.line_segments[i].start[0];
      y_start_temp = msg.line_segments[i].start[1];
      x_end_temp = msg.line_segments[i].end[0];
      y_end_temp = msg.line_segments[i].end[1];

      if (isnan(x_start_temp) || isnan(y_start_temp) || isnan(x_end_temp) || isnan(y_end_temp)) {
        continue;
      }

      x_start = y_start_temp;
      y_start = -1.0f * x_start_temp - 0.415f;
      x_end = y_end_temp;
      y_end = -1.0f * x_end_temp - 0.415f;

      if (y_start > -0.415f && y_end > -0.415f) {
        continue;
      }

      dist = getLineDist(x_start, y_start, x_end, y_end);
      len = getDist(x_start, y_start, x_end, y_end);

      if (dist < RANGE_OF_INTEREST && len > MIN_WALL_LEN) {
        line_info.push_back({dist, x_start, y_start, x_end, y_end});
      }
    }
  }

  update_1 = true;

  if (update_1 && update_2) {
    processing();
    visualize();

    update_1 = false;
    update_2 = false;
  }
}

void topic_callback_2(const laser_line_extraction::LineSegmentList msg) {
  if (update_2) return;

  if (msg.line_segments.size() > 0) {
    for (int i = 0; i < msg.line_segments.size(); i++) {
      x_start_temp = msg.line_segments[i].start[0];
      y_start_temp = msg.line_segments[i].start[1];
      x_end_temp = msg.line_segments[i].end[0];
      y_end_temp = msg.line_segments[i].end[1];

      if (isnan(x_start_temp) || isnan(y_start_temp) || isnan(x_end_temp) || isnan(y_end_temp)) {
        continue;
      }

      x_start = -1.0f * y_start_temp;
      y_start = x_start_temp + 0.415f;
      x_end = -1.0f * y_end_temp;
      y_end = x_end_temp + 0.415f;

      if (y_start < 0.415f && y_end < 0.415f) {
        continue;
      }

      dist = getLineDist(x_start, y_start, x_end, y_end);
      len = getDist(x_start, y_start, x_end, y_end);

      if (dist < RANGE_OF_INTEREST && len > MIN_WALL_LEN) {
        line_info.push_back({dist, x_start, y_start, x_end, y_end});
      }
    }
  }

  update_2 = true;

  if (update_1 && update_2) {
    processing();
    visualize();

    update_1 = false;
    update_2 = false;
  }
}

int main(int argc, char **argv) {
  ros::init(argc, argv, "processing_node");
  ros::NodeHandle n;

  ros::Subscriber subscription_1 = n.subscribe("/line_segments_1", 1, topic_callback_1);
  ros::Subscriber subscription_2 = n.subscribe("/line_segments_2", 1, topic_callback_2);
  visualize_ = n.advertise<visualization_msgs::MarkerArray>("/vis", 1);

  ros::spin();

  return 0;
}


/*
2. control to keep the distance. go find wall to certain direction and make it stop.
3. consider the angle of the wall and make it align to the wall.
4. examine the 4 direction of the wall and follow the wall CCW.
*/
