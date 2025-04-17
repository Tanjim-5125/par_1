from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
import os
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    par_1_dir = get_package_share_directory('par_1')
    aiil_rosbot_demo_dir = get_package_share_directory('aiil_rosbot_demo')

    return LaunchDescription([
        # Launch Find Object 2D from aiil_rosbot_demo
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(aiil_rosbot_demo_dir, 'launch', 'find_object_2d_robot.launch.py')
            ),
            launch_arguments={'gui': 'false'}.items()
        ),

        # Start occupancy_nav node (exploration logic)
        Node(
            package='par_1',
            executable='occupancy_nav',
            name='occupancy_nav',
            output='screen',
            parameters=[{'use_sim_time': False}]
        ),

        # Start hazard_detector node
        Node(
            package='par_1',
            executable='hazard_detector',
            name='hazard_detector',
            output='screen'
        ),
    ])
