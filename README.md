# project-turtlebot3-mapping-and-navigating

cd cd ros2_ws/

colcon build

source install/setup.bash

export TURTLEBOT3_MODEL=waffle

ros2 launch turtlebot3_gazebo simple_world.launch.py

to move the robot- in a new terminal insert:
ros2 run teleop_twist_keyboard teleop_twist_keyboard

in another teminal inset the following command to build the map:
ros2 launch turtlebot3_cartographer turtlebot3_slam_toolbox.launch.py 

now when the robot is moving it creates a map
to visualize the map in anew terminal open rviz with:

rviz2

now press add in the left side of the window, then in the new window enter "by topic" and choose the "map" topic 
