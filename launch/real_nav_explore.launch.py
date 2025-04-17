from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    slam_params = PathJoinSubstitution([FindPackageShare("par_1"), "config", "slam.yaml"])
    nav2_params = PathJoinSubstitution([FindPackageShare("par_1"), "config", "navigation_pro3.yaml"])

    return LaunchDescription([
        # SLAM Toolbox (async)
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                PathJoinSubstitution([FindPackageShare("slam_toolbox"), "launch", "online_async_launch.py"])
            ),
            launch_arguments={
                "slam_params_file": slam_params,
                "use_sim_time": "false"
            }.items(),
        ),

        # Nav2 Navigation stack
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                PathJoinSubstitution([FindPackageShare("nav2_bringup"), "launch", "navigation_launch.py"])
            ),
            launch_arguments={
                "params_file": nav2_params,
                "use_sim_time": "false",
                "autostart": "true",
                "map_subscribe_transient_local": "true"
            }.items(),
        ),

        # Custom OccupancyNav node
        Node(
            package="par_1",
            executable="occupancy_nav",
            name="occupancy_nav",
            output="screen",
            parameters=[
                {"use_sim_time": False},
                {"robot_frame": "base_link"}
            ]
        )
    ])
