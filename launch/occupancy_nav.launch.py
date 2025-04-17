from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='par_1,
            executable='occupancy_nav',
            name='occupancy_nav',
            output='screen',
            parameters=[{
                'use_sim_time': false,
                'robot_frame': 'base_link'
            }]
        )
    ])
