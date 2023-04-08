#!/usr/bin/env python3
# external
import time

# self managed
from PCANBasic import *
from connector.pcan_zlac8015d_conn import PCAN_ZLAC8015D_CONNECTION,rpm_to_hex

def tohex(val, nbits):
    return hex((val + (1 << nbits)) % (1 << nbits))
    # 16 bits if hexadecimal

class PCAN_ZLAC8015D:
    
    def __init__(self):
        print(rpm_to_hex(5,16))
        print(hex(-5))
        print(rpm_to_hex(-5,16))
        self.connection = PCAN_ZLAC8015D_CONNECTION()
        #self.connection.disconnect()
        #self.test_can_connection()
        #self.connection.start2()
        self.connection.start1()
        
        self.connection.start2()
        
        self.connection.start3()
        self.connection.start4()
        self.connection.start5()
        time.sleep(3)
        '''
        Right motor command works if these are run first!
        set_speed() = sets both wheels to go slow, documented in msg_util
        I think these should be used instead of guessing the other speeds, 
        applying these we can estimate 180 turns, and angular vel like in 
        odometry sets w ros
        '''
        self.connection.set_async()
        self.connection.set_vel_profile_on() # No setting off it seems 
        #self.connection.turn_left()
        time.sleep(3)
        self.connection.set_speed()
        time.sleep(3)
        #self.connection.start2()
        #time.sleep(3)
        #self.connection.forward_slow()
        #time.sleep(3)
        #self.connection.turn_left()
        #time.sleep(3)
        #self.connection.turn_right()
        #time.sleep(3)
        #self.connection.forward_fast()
        time.sleep(3)
        self.connection.stop_movement()
        time.sleep(3)
        self.connection.disconnect()

if __name__ == '__main__':
    pcan = PCAN_ZLAC8015D()