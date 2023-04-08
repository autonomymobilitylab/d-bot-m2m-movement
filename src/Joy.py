
#!/usr/bin/env python3
# external

from sensor_msgs.msg import Joy
import time
import rospy
import numpy as np


from geometry_msgs.msg import Twist



rospy.init_node('Joy')

vel = Twist()
Joystick = Joy()



pubCmd = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
def callback(msg):
        global pubCmd
        #print(msg)
        #self.FrontNBack
        #self.LeftNRight
        FrontNBack = msg.axes[1]
        LeftNRight = msg.axes[2]
        print("FrontNBack: {}".format(FrontNBack))
        print("LeftNRight: {}".format(LeftNRight))
        vel.angular.z = -msg.axes[2]*4
        vel.linear.x = msg.axes[1]*10
        pubCmd.publish(vel)
        #rate.sleep()
            #print("FrontNBack: {}".format(FrontNBack))
            #print("LeftNRight: {}".format(LeftNRight))
            #FNB = int(10*FrontNBack)
            #LNR = int(10*LeftNRight)
            #vel.angular.z = LNR
            #vel.linear.x = FNB
            #pubCmd.publish(vel)
            #rate.sleep()
subscriber = rospy.Subscriber('joy', Joy, callback)    
        



#pubCmd = rospy.Publisher('/cmd_vel', Twist, queue_size=1)

rate = rospy.Rate(10)
rospy.spin()

