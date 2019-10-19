# pznachi
Creation of a urdf structure for a nachi MZ04 model.

visualize in Gazebo
source ~/victor_ws/devel/setup.bash

roslaunch pznachi  gazebo.launch

Visualize in RVIZ 
source ~/victor_ws/devel/setup.bash

roslaunch pznachi  display.launch model:='$(pznachi)/urdf/pznachi.urdf'
