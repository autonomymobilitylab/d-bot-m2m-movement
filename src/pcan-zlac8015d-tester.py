#!/usr/bin/env python3
# external
import rospy
from std_msgs.msg import Int32MultiArray, Int8, Float32MultiArray, String
from nav_msgs.msg import Odometry
from tf.transformations import quaternion_from_euler
from geometry_msgs.msg import TransformStamped
import can
from can.interface import Bus
import os
from ctypes import *
from string import *
import platform
import time

# self managed
from PCANBasic import *
from connector.pcan_zlac8015d_conn import PCAN_ZLAC8015D_CONNECTION

class PCAN_ZLAC8015D:
    
    def __init__(self):
        self.connection = PCAN_ZLAC8015D_CONNECTION()
        time.sleep(3)
        self.connection.start1()
        time.sleep(3)
        self.connection.start2()
        time.sleep(3)
        self.connection.start3()
        time.sleep(3)
        self.connection.start4()
        time.sleep(3)
        self.connection.start5()
        time.sleep(3)
        self.connection.forward_slow()
        # self.can_start2()
        time.sleep(3)
        self.connection.stop_movement()
        time.sleep(3)
        self.connection.disconnect()

if __name__ == '__main__':
    pcan = PCAN_ZLAC8015D()