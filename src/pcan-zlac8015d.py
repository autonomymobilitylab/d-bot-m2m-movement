#!/usr/bin/env python
import rospy
import can
from can.interface import Bus

from ZLAC8015D import Controller as ZLAC8015D

class PCAN_ZLAC8015D:
    
    def __init__(self):
        bus = can.interface.Bus(bustype='pcan', channel='PCAN_USBBUS1',state = can.bus.BusState.PASSIVE, bitrate=500000)
        test_can_connection(bus)
        rospy.init_node('pcan_ZLAC8015D_node', anonymous=True)
        rospy.loginfo("Start pcan-ZLAC8015D node")
        ros_hello()

    def test_can_connection(bus):
        msg = can.Message(
            arbitration_id=0xC0FFEE, data=[0, 25, 0, 1, 3, 1, 4, 1], is_extended_id=True
            )
        try:
            bus.send(msg)
            print(f"Message sent on {bus.channel_info}")
        except can.CanError:
            print("Message NOT sent")
    
    def ros_hello():
        pub = rospy.Publisher('hello', String, queue_size=10)
        rate = rospy.Rate(1)
        while not rospy.is_shutdown():
            message = 'Hello, world!'
            rospy.loginfo(message)
            pub.publish(message)
            rate.sleep()

if __name__ == '__main__':
    pcan = PCAN_ZLAC8015D()