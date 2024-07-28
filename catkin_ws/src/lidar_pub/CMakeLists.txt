cmake_minimum_required(VERSION 3.0.2)
project(lidar_pub)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  sensor_msgs
)

find_package(ydlidar_sdk REQUIRED)

catkin_package()

include_directories(
  ${catkin_INCLUDE_DIRS}
  ${YDLIDAR_SDK_INCLUDE_DIRS}
)

add_executable(lidar_pub src/lidar_pub.cpp)
target_link_libraries(lidar_pub ${catkin_LIBRARIES} ${YDLIDAR_SDK_LIBRARIES})
