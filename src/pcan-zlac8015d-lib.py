#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32MultiArray, Int8, Float32MultiArray, String
from nav_msgs.msg import Odometry
from tf.transformations import quaternion_from_euler
from geometry_msgs.msg import TransformStamped
from PCANBasic import *
import can
from can.interface import Bus
import os
from ctypes import *
from string import *
import platform
import time


from ZLAC8015D import Controller as ZLAC8015D

class PCAN_ZLAC8015D:
    
    def __init__(self):
        m_objPCANBasic = PCANBasic()

        # Try different channel numbers until the correct one is found
       
        channel = PCAN_USBBUS1
        #Kaikki palauttaa vaan 5120 == it indicates that the PCAN hardware interface connected to the specified channel was not found.
        result = m_objPCANBasic.Initialize(channel, PCAN_BAUD_500K)
        print(result)
        m_objPCANBasic.Uninitialize(channel)
        if result == PCAN_ERROR_OK:
            # Found the correct channel number
            print("Channel number is:", channel)
            m_objPCANBasic.Uninitialize(channel)
        #bus = can.interface.Bus(bustype='pcan', channel='PCAN_USBBUS1',state = can.bus.BusState.PASSIVE, bitrate=500000)
        #TPCANHandle                   = c_ushort
        #PCAN_USBBUS1                  = TPCANHandle(0x51)
        # m_objPCANBasic = PCANBasic()

        # # Try different channel numbers until the correct one is found
        # for i in range(1, 40):
        #     result = m_objPCANBasic.Uninitialize(i)
        #     m_objPCANBasic.Initialize(i, PCAN_BAUD_500K)
        #     print(result)
        #     m_objPCANBasic.Uninitialize(i)
        #     if result == PCAN_ERROR_OK:
        #         # Found the correct channel number
        #         print("Channel number is:", i)
        #         #m_objPCANBasic.Uninitialize(i)
        #         break



        self.PcanHandle = channel
        print(self.PcanHandle)
        IsFD = False
        
        Bitrate = PCAN_BAUD_500K
        m_DLLFound = False
        # cHECK that not initted already
        
        self.m_objPCANBasic = PCANBasic()
        #stsResult = self.m_objPCANBasic.Read(self.PcanHandle)
        #print(stsResult)
        res = self.m_objPCANBasic.Initialize(self.PcanHandle,Bitrate)
        print(res)
        #stsResult = self.m_objPCANBasic.Read(self.PcanHandle)
        #print(stsResult)
        #self.m_objPCANBasic.Uninitialize(self.PcanHandle)
        #stsResult = self.m_objPCANBasic.Read(self.PcanHandle)
        #print(stsResult)

        #self.m_objPCANBasic.Initialize(self.PcanHandle,Bitrate)
        # try:
        #     self.m_objPCANBasic = PCANBasic()
        #     m_DLLFound = True
        # except :
        #     print("Unable to find the library: PCANBasic.dll !")
        #     m_DLLFound = False

        #bus = Bus(bustype='pcan', channel='PCAN_USBBUS1', bitrate=250000)
        #rospy.loginfo("Swocket can connected successfully!")
        #try:
        #    bus = Bus(bustype='pcan', channel='PCAN_USBBUS1', bitrate=250000)
        #    rospy.loginfo("Swocket can connected successfully!")
        #except OSError:
        #    print('Cannot find pcan channel: vcan0')
        #    rospy.loginfo("Cannot find pcan channel: vcan0")

        #self.test_can_connection(bus)
        #pub1.publish('test')
        #self.init_dbot()
        time.sleep(3)
        self.can_start1()
        time.sleep(3)
        self.can_start2()
        time.sleep(3)
        self.can_start3()
        time.sleep(3)
        self.can_start4()
        time.sleep(3)
        self.can_start5()
        time.sleep(3)
        self.can_slow_front_both()
        # self.can_start2()
        time.sleep(3)
        stsResult = self.m_objPCANBasic.Read(self.PcanHandle)
        print(stsResult)
        self.can_start2()
        self.m_objPCANBasic.Uninitialize(self.PcanHandle)
        

        

    def GetDataString(data, msgtype):
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

    def GetIdString(id, msgtype):
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


        #msg = can.Message(
        #    arbitration_id=0xC0FFEE, data=[0, 25, 0, 1, 3, 1, 4, 1], is_extended_id=False
        #    )
        #try:
        #    bus.send(msg)
        #    rospy.loginfo(f"Message sent on {bus.channel_info}")
        #except can.CanError:
        #    rospy.loginfo("Message NOT sent")
    
    def init_dbot(self):
        print('initializing dbot pcan')
        msgCanMessage = TPCANMsg()
        msgCanMessage.ID = 0x000
        msgCanMessage.LEN = 8
        msgCanMessage.MSGTYPE = PCAN_MESSAGE_STANDARD.value
        msgCanMessage.DATA=0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
        res = self.m_objPCANBasic.Write(self.PcanHandle, msgCanMessage)
        print(res)

    def can_start1(self):
        print('running can_start1')
        msgCanMessage = TPCANMsg()
        msgCanMessage.ID = 0x601
        msgCanMessage.LEN = 8
        msgCanMessage.MSGTYPE = PCAN_MESSAGE_STANDARD.value
        msgCanMessage.DATA[0]=0x01
        msgCanMessage.DATA[1]=0x00
        msgCanMessage.DATA[2]=0x00
        msgCanMessage.DATA[3]=0x00
        msgCanMessage.DATA[4]=0x00
        msgCanMessage.DATA[5]=0x00
        msgCanMessage.DATA[6]=0x00
        msgCanMessage.DATA[7]=0x00

        self.m_objPCANBasic.Write(self.PcanHandle, msgCanMessage)
        #msg = can.Message(
        #    arbitration_id=0x601, data=[0x2b, 0x40, 0x60, 0x00, 0x00, 0x00, 0x00, 0x00], is_extended_id=True
        #    )
        #bus.send(msg)
        #try:
        #    #bus.send(msg)
        #    print(f"Message sent on {bus.channel_info}")
        #except can.CanError:
        #    print("Message NOT sent")

    def can_start2(self):
        print('running can_start2')
        msgCanMessage = TPCANMsg()
        msgCanMessage.ID = 0x601
        msgCanMessage.LEN = 8
        msgCanMessage.MSGTYPE = PCAN_MESSAGE_STANDARD.value
        msgCanMessage.DATA[0]=0x2B
        msgCanMessage.DATA[1]=0x40
        msgCanMessage.DATA[2]=0x60
        msgCanMessage.DATA[3]=0x00
        msgCanMessage.DATA[4]=0x00
        msgCanMessage.DATA[5]=0x00
        msgCanMessage.DATA[6]=0x00
        msgCanMessage.DATA[7]=0x00

        self.m_objPCANBasic.Write(self.PcanHandle, msgCanMessage)
        #msg = can.Message(
        #    arbitration_id=0x601, data=[0x2b, 0x40, 0x60, 0x00, 0x00, 0x00, 0x00, 0x00], is_extended_id=True
        #    )
        #try:
        #    bus.send(msg)
        #    print(f"Message sent on {bus.channel_info}")
        #except can.CanError:
        #    print("Message NOT sent")


    def can_start3(self):
        print('running can_start3')
        msgCanMessage = TPCANMsg()
        msgCanMessage.ID = 0x601 
        msgCanMessage.LEN = 8
        msgCanMessage.MSGTYPE = PCAN_MESSAGE_STANDARD.value
        msgCanMessage.DATA[0]=0x2B
        msgCanMessage.DATA[1]=0x40
        msgCanMessage.DATA[2]=0x60
        msgCanMessage.DATA[3]=0x00
        msgCanMessage.DATA[4]=0x06
        msgCanMessage.DATA[5]=0x00
        msgCanMessage.DATA[6]=0x00
        msgCanMessage.DATA[7]=0x00

        self.m_objPCANBasic.Write(self.PcanHandle, msgCanMessage)
        #msg = can.Message(
        #    arbitration_id=0x601, data=[0x2b, 0x40, 0x60, 0x00, 0x00, 0x00, 0x00, 0x00], is_extended_id=True
        #    )
        #try:
        #    bus.send(msg)
        #    print(f"Message sent on {bus.channel_info}")
        #except can.CanError:
        #    print("Message NOT sent")
    


    def can_start4(self):
        print('running can_start4')
        msgCanMessage = TPCANMsg()
        msgCanMessage.ID = 0x601
        msgCanMessage.LEN = 8
        msgCanMessage.MSGTYPE = PCAN_MESSAGE_STANDARD.value
        msgCanMessage.DATA[0]=0x2B
        msgCanMessage.DATA[1]=0x40
        msgCanMessage.DATA[2]=0x60
        msgCanMessage.DATA[3]=0x00
        msgCanMessage.DATA[4]=0x07
        msgCanMessage.DATA[5]=0x00
        msgCanMessage.DATA[6]=0x00
        msgCanMessage.DATA[7]=0x00

        self.m_objPCANBasic.Write(self.PcanHandle, msgCanMessage)

    def can_start5(self):
        print('running can_start5')
        msgCanMessage = TPCANMsg()
        msgCanMessage.ID = 0x601
        msgCanMessage.LEN = 8
        msgCanMessage.MSGTYPE = PCAN_MESSAGE_STANDARD.value
        msgCanMessage.DATA[0]=0x2B
        msgCanMessage.DATA[1]=0x40
        msgCanMessage.DATA[2]=0x60
        msgCanMessage.DATA[3]=0x00
        msgCanMessage.DATA[4]=0x0F
        msgCanMessage.DATA[5]=0x00
        msgCanMessage.DATA[6]=0x00
        msgCanMessage.DATA[7]=0x00

        self.m_objPCANBasic.Write(self.PcanHandle, msgCanMessage)

    def can_slow_front_both(self):
        print('running can_slow_front_both')
        msgCanMessage = TPCANMsg()
        msgCanMessage.ID = 0x601
        msgCanMessage.LEN = 8
        msgCanMessage.MSGTYPE = PCAN_MESSAGE_STANDARD.value
        msgCanMessage.DATA[0]=0x23
        msgCanMessage.DATA[1]=0xFF
        msgCanMessage.DATA[2]=0x60
        msgCanMessage.DATA[3]=0x03
        msgCanMessage.DATA[4]=0x05
        msgCanMessage.DATA[5]=0x00
        msgCanMessage.DATA[6]=0xFA
        msgCanMessage.DATA[7]=0xFF

        self.m_objPCANBasic.Write(self.PcanHandle, msgCanMessage)
        stsResult = self.m_objPCANBasic.Read(self.PcanHandle)
        print(stsResult[0])
        if stsResult[0] == PCAN_ERROR_OK:
        ## We show the received message
        #ProcessMessageCanFd(stsResult[1],stsResult[2])
            id = GetIdString(msgCanMessage.ID,msgCanMessage.MSGTYPE)
            daatta = GetDataString(msgCanMessage.DATA,msgCanMessage.MSGTYPE)
            print("READ: " + "ID: ",id , daatta)

if __name__ == '__main__':
    pcan = PCAN_ZLAC8015D()