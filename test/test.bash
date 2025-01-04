#!/bin/bash

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc

ng() {
    echo "NG at Line $1"
    res=1
}

res=0

{
ros2 run mypkg system_status_publisher
}&
{
  sleep 10
  echo ""
  system_status_log=$(ros2 topic echo /system_ststus--once)
  echo "$system_status_log"

  echo "$system_status_log" | grep -E 'CPU:' || ng ${LINENO}
  echo "$system_status_log" | grep -E 'Memory:' || ng ${LINENO}
  echo "$system_status_log" | grep -E 'Disk:' || ng ${LINENO}
}
echo ""

sleep 10

[ "$res" = 0 ] && echo "OK"
exit $res
