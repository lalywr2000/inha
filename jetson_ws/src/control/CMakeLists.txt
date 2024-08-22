cmake_minimum_required(VERSION 3.0.2)
project(control)

find_package(catkin REQUIRED COMPONENTS
  rospy
  laser_line_extraction_msg
)

catkin_package()

include_directories(
  ${catkin_INCLUDE_DIRS}
)

catkin_install_python(PROGRAMS
  src/control.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
