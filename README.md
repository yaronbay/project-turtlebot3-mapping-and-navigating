# project-turtlebot3-mapping-and-navigating
this project is about mapping and navigating in a map with obsticales
in this project i use the turtulebot3 (waffle model) package via ros2 humble distribution and gazebo fortress
for more information about turtlebot3:

https://emanual.robotis.com/docs/en/platform/turtlebot3/overview/

i have used the skelaton to this package and created/added/edited/deleted files so the package can execute the assingment

requirments:
ros2 humble - https://docs.ros.org/en/humble/Installation.html

gazebo - https://gazebosim.org/docs

the following ros packages are required: 
gazebo_ros_pkgs - sudo apt install ros-humble-gazebo-ros-pkgs

ros navigation2 -  sudo apt install ros-humble-navigation2 ros-humble-nav2-bringup

ros slam toolbox - sudo apt-get install ros-humble-slam-toolbox

ros teleop twist keyboard- sudo apt install ros-humble-teleop-twist-keyboard



now download and extract the zip file into your ros2_ws/src/ or use the clone option:
in the terminal copy the following lines:

cd ros2_ws/src/

git clone https://github.com/yaronbay/project-turtlebot3-mapping-and-navigating.git

now fo back to your workspace and build:

cd ..

(before building make sure to be in the ros2_ws directory)

colcon build

source install/setup.bash

choose the waffle model:

export TURTLEBOT3_MODEL=waffle

now launch the custom simple world and thw waffle model:

ros2 launch turtlebot3_gazebo simple_world.launch.py

to move the robot- in a new terminal insert:

ros2 run teleop_twist_keyboard teleop_twist_keyboard

in another terminal insert the following command to build the map:
ros2 launch turtlebot3_cartographer turtlebot3_slam_toolbox.launch.py 

now when the robot is moving it creates a map
to visualize the map in anew terminal open rviz in a new terminal with:

rviz2

now press add in the left side of the window, then in the new window enter "by topic" and choose the "map" topic, also it is possible to wach the datafrom the sensors choosing pointcloud2 for the depth camera or the laserscan to watch the lidar. i didnt managed to get a good visualization of the IMU so if you with to get a signal you can enter in a new terminal:

ros2 topic echo /imu 

for the following part i didnt managed to set the nav2 packaged properly and i had trouble with the cpp node- had problems to call certain libraries, unfortunatley i coudlnt solve these problems on time so currently it is possible to move the robot only manualy with the teleop_twist_keyboard

*two more minor problems that i have noticed is that the robot is not spwaning in the beginning and the map building visualization is not static in rviz, those problems are worth to mention but overall not that significant.
