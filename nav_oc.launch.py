from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='par_1',
            executable='nav_oc',
            name='nav_oc',
            output='screen',
            parameters=[{
                'use_sim_time': False,
                'robot_frame': 'base_link'
            }]
        )
    ])
