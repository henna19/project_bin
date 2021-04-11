#!/bin/bash

dir=$(pwd)
cd ..
cd ..
dir=$(pwd)
source $dir/devel/setup.bash #sourcing the ROS package

gnome-terminal --tab --title="terminal 1" -- sh -c 'rostopic echo /bin_state | bash'
#roslaunch bin_projet bin_s.launch 

sleep 5s

rosservice call /bin_state_server "id_poubelle:
  data: 1
state:
  data: 1"

sleep 4s

rosservice call /bin_state_server "id_poubelle:
  data: 4
state:
  data: 1"


sleep 6s

rosservice call /bin_state_server "id_poubelle:
  data: 2
state:
  data: 1"
