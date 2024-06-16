import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration


def generate_launch_description():
    use_sim_time = LaunchConfiguration('use_sim_time', default='true')
    namespace = LaunchConfiguration('namespace', default='')
    map_yaml_file = LaunchConfiguration('map', default=os.path.join(
        get_package_share_directory('turtlebot3_navigation2'),
        'map',
        'map.yaml'))
    param_file = LaunchConfiguration('params_file', default=os.path.join(
        get_package_share_directory('turtlebot3_navigation2'),
        'param',
        'nav2_params.yaml'))

    return LaunchDescription([
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='true',
            description='Use simulation (Gazebo) clock if true'),

        DeclareLaunchArgument(
            'namespace',
            default_value='',
            description='Namespace'),

        DeclareLaunchArgument(
            'map',
            default_value=map_yaml_file,
            description='Full path to map file to load'),

        DeclareLaunchArgument(
            'params_file',
            default_value=param_file,
            description='Full path to the ROS2 parameters file to use'),

        Node(
            package='nav2_bringup',
            executable='bringup_launch.py',
            output='screen',
            parameters=[param_file],
            arguments=['--map', map_yaml_file, '--use_sim_time', use_sim_time]
        )
    ])
