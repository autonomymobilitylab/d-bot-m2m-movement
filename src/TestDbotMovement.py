#!/usr/bin/env python3
# external
import time
import rospy
import numpy as np

from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy
# self managed
from PCANBasic import *
from connector.pcan_zlac8015d_conn import PCAN_ZLAC8015D_CONNECTION,rpm_to_hex,lin_ang_to_wheel_speed




def tohex(val, nbits):
    return hex((val + (1 << nbits)) % (1 << nbits))
    # 16 bits if hexadecimal

class PCAN_ZLAC8015D:
    
    def __init__(self):
        self.connection = PCAN_ZLAC8015D_CONNECTION()
        #print(rpm_to_hex(5,16))
        #print(hex(-5))
        #print(rpm_to_hex(-5,16))
        #self.connection.disconnect()
        #self.test_can_connection()
        #self.connection.start2()
        #self.connection.start1()
        
        #self.connection.start2()
        
        #self.connection.start3()
        #self.connection.start4()
        #self.connection.start5()
        #time.sleep(3)
        '''
        Right motor command works if these are run first!
        set_speed() = sets both wheels to go slow, documented in msg_util
        I think these should be used instead of guessing the other speeds, 
        applying these we can estimate 180 turns, and angular vel like in 
        odometry sets w ros
        '''
        #self.connection.set_async()
        #elf.connection.set_vel_profile_on() # No setting off it seems 
        #self.connection.turn_left()
        #time.sleep(3)
        #self.connection.set_speed()
        #time.sleep(3)
        #self.connection.start2()
        #time.sleep(3)
        #self.connection.forward_slow()
        #time.sleep(3)
        #self.connection.turn_left()
        #time.sleep(3)
        #self.connection.turn_right()
        #time.sleep(3)
        #self.connection.forward_fast()
        #time.sleep(3)
        #self.connection.stop_movement()
        #time.sleep(3)
        #self.connection.disconnect()

#if __name__ == '__main__':
pcan = PCAN_ZLAC8015D()
pcan.connection.start1()
pcan.connection.start2()
pcan.connection.start3()
pcan.connection.start4()
pcan.connection.start5()
pcan.connection.set_async()
pcan.connection.set_vel_profile_on()
pcan.connection.set_right_motor_acceleration()
pcan.connection.set_left_motor_acceleration()
pcan.connection.set_right_motor_deceleration()
pcan.connection.set_left_motor_deceleration()

def callback(msg):
    Lvel = msg.linear.x
    Avel = msg.angular.z
    print("Linear: {}".format(Lvel))
    print("Angular: {}".format(Avel))
    velR, velL = lin_ang_to_wheel_speed(int(Avel), int(Lvel))

    velR = rpm_to_hex(int(velR), 16)
    velL = rpm_to_hex(int(velL), 16)
    print(velL)
    print(velR)
    pcan.connection.set_speed(velR, velL)
    
subCmd = rospy.Subscriber('/cmd_vel', Twist, callback)

rospy.init_node('TestDbotMovement')
print("TestDbotMovement initialized!")

rate = rospy.Rate(5)
while not rospy.is_shutdown():
    rate.sleep()
