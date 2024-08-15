#include "rclcpp/rclcpp.hpp"

#include "sensor_msgs/msg/laser_scan.hpp"

#include <string>
#include <vector>
#include <cmath>

using std::placeholders::_1;

#define VIEW_ANGLE_DEG 180.0f


sensor_msgs::msg::LaserScan scan_1;
sensor_msgs::msg::LaserScan scan_2;

bool update_1 = false;
bool update_2 = false;


class Fusion : public rclcpp::Node
{
public:
  Fusion()
  : Node("fusion_node")
  {
    subscription_1 = this->create_subscription<sensor_msgs::msg::LaserScan>(
      "/scan_1", 1, std::bind(&Fusion::topic_callback_1, this, _1));

    subscription_2 = this->create_subscription<sensor_msgs::msg::LaserScan>(
      "/scan_2", 1, std::bind(&Fusion::topic_callback_2, this, _1));

    publication_ = this->create_publisher<sensor_msgs::msg::LaserScan>(
      "/fusion", 1);

    fusion_data.header.frame_id = "laser_fusion";
    fusion_data.angle_min = -180.0f;
    fusion_data.angle_max = 180.0f;
    fusion_data.range_min = 0.12f;
    fusion_data.range_max = 10.0f;
    fusion_data.intensities.resize(0);
  }

private:
  void fusion_pub()
  {
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
      fusion_data.ranges.push_back(temp[(temp_size + i - 293) % temp_size]);
    }

    fusion_data.angle_increment = 3.14159f * 2.0f / temp_size;

    publication_->publish(fusion_data);
    // RCLCPP_INFO(this->get_logger(), "");
  }

  void topic_callback_1(const sensor_msgs::msg::LaserScan::SharedPtr msg)
  {
    scan_1.ranges = msg->ranges;
    scan_1.angle_increment = msg->angle_increment;
    update_1 = true;

    if (update_1 && update_2)
    {
      fusion_pub();

      update_1 = false;
      update_2 = false;
    }
  }

  void topic_callback_2(const sensor_msgs::msg::LaserScan::SharedPtr msg)
  {
    scan_2.ranges = msg->ranges;
    scan_2.angle_increment = msg->angle_increment;
    update_2 = true;

    if (update_1 && update_2)
    {
      fusion_pub();

      update_1 = false;
      update_2 = false;
    }
  }

  rclcpp::Subscription<sensor_msgs::msg::LaserScan>::SharedPtr subscription_1;
  rclcpp::Subscription<sensor_msgs::msg::LaserScan>::SharedPtr subscription_2;
  rclcpp::Publisher<sensor_msgs::msg::LaserScan>::SharedPtr publication_;

  sensor_msgs::msg::LaserScan fusion_data;
  std::vector<float> temp;
  size_t point_size_1, point_size_2, temp_size;
  int idx;
};


int main(int argc, char * argv[])
{
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<Fusion>());
  rclcpp::shutdown();

  return 0;
}
