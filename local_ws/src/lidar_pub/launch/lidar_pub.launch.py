from launch import LaunchDescription
from launch_ros.actions import Node

lidar_to_center_dist = 0.45 / 2  # [m]

def generate_launch_description():
    lidar_pub_1 = Node(
        package='lidar_pub',
        executable='lidar_pub_1',
        output='screen',
    )
    lidar_pub_2 = Node(
        package='lidar_pub',
        executable='lidar_pub_2',
        output='screen',
    )
    fusion = Node(
        package='lidar_pub',
        executable='fusion',
        output='screen',
    )

    return LaunchDescription(
        [
            lidar_pub_1,
            lidar_pub_2,
            fusion,
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
            Node(
                package='tf2_ros',
                executable='static_transform_publisher',
                arguments = ['0', '0', '0', '0', '0', '0', 'base_link', 'laser_fusion']
            ),
        ]
    )
