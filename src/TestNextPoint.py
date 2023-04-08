#Ignore this

import time
import rospy
import numpy as np

from geometry_msgs.msg import Pose
from nav_msgs.msg import Odometry


def callback(msg):
    if(ilmatar):
        next = [ilmatar.x,ilmatar.y,0]
    else:
        next = [1,1,0]


rospy.init_node('TestNextPoint')

#sub = rospy.Subscriber('', ilmatar, callback)
#pub = rospy.Pubisher('/cmd_vel', Pose, queue_size = 0)

rate = rospy.Rate(10)
while not rospy.is_shutdown():
    pub.publish(point)
    rate.sleep()
