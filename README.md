# project-turtlebot3-mapping-and-navigating
this project is about mapping and navigating in a map with obsticales
in this project i use the turtulebot3 (waffle model) package via ros2 humble distribution and gazebo fortress
for more information about turtlebot3:


requirments:
ros2 humble - https://docs.ros.org/en/humble/Installation.html
gazebo - https://gazebosim.org/docs

the following ros packages are required: 
gazebo_ros_pkgs - sudo apt install ros-humble-gazebo-ros-pkgs
ros navigation2 -  sudo apt install ros-humble-navigation2 ros-humble-nav2-bringup
ros slam toolbox - sudo apt-get install ros-humble-slam-toolbox
ros teleop twist keyboard- sudo apt install ros-humble-teleop-twist-keyboard


cd ros2_ws/

colcon build

source install/setup.bash

export TURTLEBOT3_MODEL=waffle

ros2 launch turtlebot3_gazebo simple_world.launch.py

to move the robot- in a new terminal insert:
ros2 run teleop_twist_keyboard teleop_twist_keyboard

in another terminal insert the following command to build the map:
ros2 launch turtlebot3_cartographer turtlebot3_slam_toolbox.launch.py 

now when the robot is moving it creates a map
to visualize the map in anew terminal open rviz with:

rviz2

now press add in the left side of the window, then in the new window enter "by topic" and choose the "map" topic 
