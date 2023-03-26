#!/usr/bin/env python3
# external
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