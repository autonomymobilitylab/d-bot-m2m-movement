#!/usr/bin/env python3
from PCANBasic import *
from ctypes import *
from string import *
from util.zlac8015d_msg_util import ZLAC8015dMsgUtil

def lin_ang_to_wheel_speed(ang,lin):
    # transforms wanted linear and angular speeds (x and z) into wheel speeds (rigth,left)
    # When called, set (ang,lin)

    # Set correct wheel dist and radius:
    wheel_dist = 1
    wheel_r = 0.2032 #cm?
    # Calculations:
    right= (ang + lin * wheel_dist / 2) / wheel_r
    left = (ang - lin* wheel_dist / 2) / wheel_r
    return right,left

def rpm_to_hex(val, nbits):
    # Give wanted rpm and 16 nbits, outputs direction (FF or 00) and 
    h = hex((val + (1 << nbits)) % (1 << nbits))
    h = int(h,16)
    dir, vel = hex(h>> 8), hex(h & 0xFF)
    return (int(dir,16),int(vel,16))
    # 16 bits if hexadecimal

class PCAN_ZLAC8015D_CONNECTION:

    def __init__(self):
        
        self.m_objPCANBasic = PCANBasic()
        self.channel = PCAN_USBBUS1
        self.pcan_handle = self.channel
        self.msg_util = ZLAC8015dMsgUtil()
        #self.disconnect()
        self.connect()
        self.test_can_connection(self.channel)

    def connect(self):
       # result = self.m_objPCANBasic.Uninitialize(self.channel)
        result = self.m_objPCANBasic.Initialize(self.channel, PCAN_BAUD_500K)
        
        # temporary logging
        self.degug_log(result)
        self.m_objPCANBasic.Uninitialize(self.channel)
        if result == PCAN_ERROR_OK:
            print("Channel number is:", self.channel)
            self.m_objPCANBasic.Uninitialize(self.channel)

        self.pcan_handle = self.channel
        self.degug_log(self.pcan_handle)

        Bitrate = PCAN_BAUD_500K

        self.m_objPCANBasic = PCANBasic()
        res = self.m_objPCANBasic.Initialize(self.pcan_handle, Bitrate)
        self.degug_log(res)

    def disconnect(self):
        self.degug_log('disconnecting')
        res = self.m_objPCANBasic.Uninitialize(self.pcan_handle)
        self.degug_log(res)


    def get_data_string(self, data, msgtype):
        """
        Gets the data of a CAN message as a string

        Parameters:
            data = Array of bytes containing the data to parse
            msgtype = Type flags of the message the data belong

        Returns:
            A string with hexadecimal formatted data bytes of a CAN message
        """
        if (msgtype & PCAN_MESSAGE_RTR.value) == PCAN_MESSAGE_RTR.value:
            return "Remote Request"
        else:
            strTemp = b""
            for x in data:
                strTemp += b'%.2X ' % x
            return str(strTemp).replace("'","",2).replace("b","",1)

    def get_id_string(self,id, msgtype):
        """
        Gets the string representation of the ID of a CAN message

        Parameters:
            id = Id to be parsed
            msgtype = Type flags of the message the Id belong

        Returns:
            Hexadecimal representation of the ID of a CAN message
        """
        if (msgtype & PCAN_MESSAGE_STANDARD.value) == PCAN_MESSAGE_STANDARD.value:
            return '%.8Xh' %id
        else:
            return '%.3Xh' %id

    def test_can_connection(self, bus):
        msgCanMessage = TPCANMsg()
        msgCanMessage.ID = 0x0c72 
        msgCanMessage.LEN = 8
        msgCanMessage.MSGTYPE = PCAN_MESSAGE_STANDARD.value

    def start1(self):
        res = self.m_objPCANBasic.Write(self.pcan_handle, self.msg_util.get_start1_msg())
        self.degug_log(res)

    def start2(self):
        res = self.m_objPCANBasic.Write(self.pcan_handle, self.msg_util.get_start2_msg())
        self.degug_log(res)

    def start3(self):
        res = self.m_objPCANBasic.Write(self.pcan_handle, self.msg_util.get_start3_msg())
        self.degug_log(res)

    def start4(self):
        self.m_objPCANBasic.Write(self.pcan_handle, self.msg_util.get_start4_msg())

    def start5(self):
        self.m_objPCANBasic.Write(self.pcan_handle, self.msg_util.get_start5_msg())

    def forward_slow(self):
        self.m_objPCANBasic.Write(self.pcan_handle, self.msg_util.get_slow_move_forward_message())

    def forward_fast(self):
        self.m_objPCANBasic.Write(self.pcan_handle, self.msg_util.get_fast_move_forward_message())

    def turn_left(self):
        self.m_objPCANBasic.Write(self.pcan_handle, self.msg_util.get_turn_left_message())

    def turn_right(self):
        self.m_objPCANBasic.Write(self.pcan_handle, self.msg_util.get_turn_right_message())
    
    def stop_movement(self):
        self.m_objPCANBasic.Write(self.pcan_handle, self.msg_util.get_start2_msg())

    def set_async(self):
        self.m_objPCANBasic.Write(self.pcan_handle,self.msg_util.get_set_async_control())

    def set_right_motor_acceleration(self):
        self.m_objPCANBasic.Write(self.pcan_handle,self.msg_util.get_set_right_motor_acceleration())

    def set_left_motor_acceleration(self):
        self.m_objPCANBasic.Write(self.pcan_handle,self.msg_util.get_set_left_motor_acceleration())

    def set_right_motor_deceleration(self):
        self.m_objPCANBasic.Write(self.pcan_handle,self.msg_util.get_set_right_motor_deceleration())

    def set_left_motor_deceleration(self):
        self.m_objPCANBasic.Write(self.pcan_handle,self.msg_util.get_set_left_motor_deceleration())
    
    def set_vel_profile_on(self):
        self.m_objPCANBasic.Write(self.pcan_handle,self.msg_util.get_set_vel_profile())

    def set_speed(self, velR, velL):
        res1 = self.m_objPCANBasic.Write(self.pcan_handle,self.msg_util.get_set_speed_left_test(velR))
        res2 = self.m_objPCANBasic.Write(self.pcan_handle,self.msg_util.get_set_speed_right_test(velL))
        self.degug_log(res1)
        self.degug_log(res2)
    def degug_log(self, result):
        print(result)
