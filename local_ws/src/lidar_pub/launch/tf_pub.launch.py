from launch import LaunchDescription
from launch_ros.actions import Node

lidar_to_center_dist = 0.45 / 2  # [m]

def generate_launch_description():
    return LaunchDescription(
        [
            Node(
                package='tf2_ros',
                executable='static_transform_publisher',
                arguments = [str(lidar_to_center_dist * 1.0), '0', '0', '0', '0', '0', 'base_link', 'laser_1']
            ),
            Node(
                package='tf2_ros',
                executable='static_transform_publisher',
                arguments = [str(lidar_to_center_dist * -1.0), '0', '0', '3.14159', '0', '0', 'base_link', 'laser_2']
            ),
        ]
    )
