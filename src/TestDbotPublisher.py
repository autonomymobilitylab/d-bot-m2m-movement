#!/usr/bin/env python3
# external
import time
import rospy
import numpy as np


from geometry_msgs.msg import Twist


rospy.init_node('TestDbotPublisher')


pubCmd = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
vel = Twist()
rate = rospy.Rate(0.25)
while not rospy.is_shutdown():
    i= int(input("x vel"))
    j = int(input("z vel"))
    vel.angular.z = j
    vel.linear.x = i
    pubCmd.publish(vel)
    rate.sleep()


    #vel.angular.z = 5
    #vel.linear.x = 0
    #pubCmd.publish(vel)
    #rate.sleep()10


