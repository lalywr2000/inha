cmake_minimum_required(VERSION 3.0.2)
project(lidar_pub)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  std_msgs
)

catkin_package()

include_directories(
  ${catkin_INCLUDE_DIRS}
)

add_executable(std_pub src/std_pub.cpp)
target_link_libraries(std_pub ${catkin_LIBRARIES})

add_executable(std_sub src/std_sub.cpp)
target_link_libraries(std_sub ${catkin_LIBRARIES})
