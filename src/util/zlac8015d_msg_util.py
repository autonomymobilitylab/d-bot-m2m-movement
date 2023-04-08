import numpy as np

from PCANBasic import *

class ZLAC8015dMsgUtil:

    def __init__(self):
        return

    def get_start1_msg(self):
        # Node to operating state
        print('running can_start1')
        msgCanMessage = TPCANMsg()
        msgCanMessage.ID = 0x000
        msgCanMessage.LEN = 8
        msgCanMessage.MSGTYPE = PCAN_MESSAGE_STANDARD.value
        msgCanMessage.DATA[0] = 0x01
        msgCanMessage.DATA[1] = 0x00
        msgCanMessage.DATA[2] = 0x00
        msgCanMessage.DATA[3] = 0x00
        msgCanMessage.DATA[4] = 0x00
        msgCanMessage.DATA[5] = 0x00
        msgCanMessage.DATA[6] = 0x00
        msgCanMessage.DATA[7] = 0x00
        return msgCanMessage

    def get_start2_msg(self):
        # Initialization step 0
        print('running can_start2')
        msgCanMessage = TPCANMsg()
        msgCanMessage.ID = 0x601
        msgCanMessage.LEN = 8
        msgCanMessage.MSGTYPE = PCAN_MESSAGE_STANDARD.value
        msgCanMessage.DATA[0] = 0x2B
        msgCanMessage.DATA[1] = 0x40
        msgCanMessage.DATA[2] = 0x60
        msgCanMessage.DATA[3] = 0x00
        msgCanMessage.DATA[4] = 0x00
        msgCanMessage.DATA[5] = 0x00
        msgCanMessage.DATA[6] = 0x00
        msgCanMessage.DATA[7] = 0x00
        return msgCanMessage

    def get_start3_msg(self):
        # Initialization step 1
        print('running can_start3')
        msgCanMessage = TPCANMsg()
        msgCanMessage.ID = 0x601
        msgCanMessage.LEN = 8
        msgCanMessage.MSGTYPE = PCAN_MESSAGE_STANDARD.value
        msgCanMessage.DATA[0] = 0x2B
        msgCanMessage.DATA[1] = 0x40
        msgCanMessage.DATA[2] = 0x60
        msgCanMessage.DATA[3] = 0x00
        msgCanMessage.DATA[4] = 0x06
        msgCanMessage.DATA[5] = 0x00
        msgCanMessage.DATA[6] = 0x00
        msgCanMessage.DATA[7] = 0x00
        return msgCanMessage

    def get_start4_msg(self):
        # Initialization step 2
        print('running can_start4')
        msgCanMessage = TPCANMsg()
        msgCanMessage.ID = 0x601
        msgCanMessage.LEN = 8
        msgCanMessage.MSGTYPE = PCAN_MESSAGE_STANDARD.value
        msgCanMessage.DATA[0] = 0x2B
        msgCanMessage.DATA[1] = 0x40
        msgCanMessage.DATA[2] = 0x60
        msgCanMessage.DATA[3] = 0x00
        msgCanMessage.DATA[4] = 0x07
        msgCanMessage.DATA[5] = 0x00
        msgCanMessage.DATA[6] = 0x00
        msgCanMessage.DATA[7] = 0x00
        return msgCanMessage

    def get_start5_msg(self):
        # Initialization step 3
        print('running can_start5')
        msgCanMessage = TPCANMsg()
        msgCanMessage.ID = 0x601
        msgCanMessage.LEN = 8
        msgCanMessage.MSGTYPE = PCAN_MESSAGE_STANDARD.value
        msgCanMessage.DATA[0] = 0x2B
        msgCanMessage.DATA[1] = 0x40
        msgCanMessage.DATA[2] = 0x60
        msgCanMessage.DATA[3] = 0x00
        msgCanMessage.DATA[4] = 0x0F
        msgCanMessage.DATA[5] = 0x00
        msgCanMessage.DATA[6] = 0x00
        msgCanMessage.DATA[7] = 0x00
        return msgCanMessage

    def get_slow_move_forward_message(self):
        print('running can_slow_front_both')
        msgCanMessage = TPCANMsg()
        msgCanMessage.ID = 0x601
        msgCanMessage.LEN = 8
        msgCanMessage.MSGTYPE = PCAN_MESSAGE_STANDARD.value
        msgCanMessage.DATA[0] = 0x23
        msgCanMessage.DATA[1] = 0xFF
        msgCanMessage.DATA[2] = 0x60
        msgCanMessage.DATA[3] = 0x03
        msgCanMessage.DATA[4] = 0x05
        msgCanMessage.DATA[5] = 0x00
        msgCanMessage.DATA[6] = 0xFA
        msgCanMessage.DATA[7] = 0xFF
        return msgCanMessage

    def get_fast_move_forward_message(self):
        print('running can_fast_front_both')
        # 23h FFh 60h 03h 50h 00h 50h FFh
        msgCanMessage = TPCANMsg()
        msgCanMessage.ID = 0x601
        msgCanMessage.LEN = 8
        msgCanMessage.MSGTYPE = PCAN_MESSAGE_STANDARD.value
        msgCanMessage.DATA[0] = 0x23
        msgCanMessage.DATA[1] = 0xFF
        msgCanMessage.DATA[2] = 0x60
        msgCanMessage.DATA[3] = 0x03
        msgCanMessage.DATA[4] = 0x50
        msgCanMessage.DATA[5] = 0x00
        msgCanMessage.DATA[6] = 0x50
        msgCanMessage.DATA[7] = 0xFF
        return msgCanMessage

    def get_turn_right_message(self):
        print('running left motor')
        # 23h FFh 60h 03h 00h 01h 00h 00h
        msgCanMessage = TPCANMsg()
        msgCanMessage.ID = 0x601
        msgCanMessage.LEN = 8
        msgCanMessage.MSGTYPE = PCAN_MESSAGE_STANDARD.value
        msgCanMessage.DATA[0] = 0x23
        msgCanMessage.DATA[1] = 0xFF
        msgCanMessage.DATA[2] = 0x60
        msgCanMessage.DATA[3] = 0x03
        msgCanMessage.DATA[4] = 0x00
        msgCanMessage.DATA[5] = 0x01
        msgCanMessage.DATA[6] = 0x00
        msgCanMessage.DATA[7] = 0x00
        return msgCanMessage

    def get_turn_left_message(self):
        print('running right motor, might not work')
        # 23h FFh 60h 02h 00h 01h 00h 00h, seems to be incorrect message data
        msgCanMessage = TPCANMsg()
        msgCanMessage.ID = 0x601
        msgCanMessage.LEN = 8
        msgCanMessage.MSGTYPE = PCAN_MESSAGE_STANDARD.value
        msgCanMessage.DATA[0] = 0x23
        msgCanMessage.DATA[1] = 0xFF
        msgCanMessage.DATA[2] = 0x60
        msgCanMessage.DATA[3] = 0x02
        msgCanMessage.DATA[4] = 0x00
        msgCanMessage.DATA[5] = 0x01
        msgCanMessage.DATA[6] = 0x00
        msgCanMessage.DATA[7] = 0x00
        return msgCanMessage
    
    def get_set_async_control(self):
        print('set async control on')
        # set asynchronous mode
        msgCanMessage = TPCANMsg()
        msgCanMessage.ID = 0x601
        msgCanMessage.LEN = 8
        msgCanMessage.MSGTYPE = PCAN_MESSAGE_STANDARD.value
        msgCanMessage.DATA[0] = 0x2B
        msgCanMessage.DATA[1] = 0x0F
        msgCanMessage.DATA[2] = 0x20
        msgCanMessage.DATA[3] = 0x00
        msgCanMessage.DATA[4] = 0x00
        msgCanMessage.DATA[5] = 0x00
        msgCanMessage.DATA[6] = 0x00
        msgCanMessage.DATA[7] = 0x00
        return msgCanMessage
    
    def get_set_vel_profile(self):
        print('set vel profile mode on')
        # set profile velocity mode
        msgCanMessage = TPCANMsg()
        msgCanMessage.ID = 0x601
        msgCanMessage.LEN = 8
        msgCanMessage.MSGTYPE = PCAN_MESSAGE_STANDARD.value
        msgCanMessage.DATA[0] = 0x2f
        msgCanMessage.DATA[1] = 0x60
        msgCanMessage.DATA[2] = 0x60
        msgCanMessage.DATA[3] = 0x00
        msgCanMessage.DATA[4] = 0x66
        msgCanMessage.DATA[5] = 0x00
        msgCanMessage.DATA[6] = 0x00
        msgCanMessage.DATA[7] = 0x00
        return msgCanMessage
    
    def get_set_speed_left_test(self,vel):
        #print('set speed of left to low')
        # Sets speed of one wheel
        # LEFT POSITIVE
        msgCanMessage = TPCANMsg()
        msgCanMessage.ID = 0x601
        msgCanMessage.LEN = 8
        msgCanMessage.MSGTYPE = PCAN_MESSAGE_STANDARD.value
        msgCanMessage.DATA[0] = 0x23
        msgCanMessage.DATA[1] = 0xFF
        msgCanMessage.DATA[2] = 0x60
        msgCanMessage.DATA[3] = 0x1 # this chooses the wheel 01 = left, 02 = right. 
        msgCanMessage.DATA[4] = vel[1] # Set speed (remember conversion, found in file to be run) Vel
        msgCanMessage.DATA[5] = vel[0] #(HEX signed 2s complement) position (00 pos, FF neg) Dir 
        msgCanMessage.DATA[6] = 0x00 # empty in this case
        msgCanMessage.DATA[7] = 0x00 # Empty
        return msgCanMessage

    def get_set_speed_right_test(self,vel):
        #print('set speed of right to low')
        # Sets speed of one wheel
        # TODO: impplementation of scaling speed set for both wheels, then we can use odometry code more easy
        # RIGHT NEGATIVE
    
        msgCanMessage = TPCANMsg()
        msgCanMessage.ID = 0x601
        msgCanMessage.LEN = 8
        msgCanMessage.MSGTYPE = PCAN_MESSAGE_STANDARD.value
        msgCanMessage.DATA[0] = 0x23
        msgCanMessage.DATA[1] = 0xFF
        msgCanMessage.DATA[2] = 0x60
        msgCanMessage.DATA[3] = 0x02 # this chooses the wheel 01 = left, 02 = right. 
        msgCanMessage.DATA[4] = vel[1]# chooses small speed? 01 == slow, 00 = none, FF = fast (sets counter clockwise moment) # Vel
        msgCanMessage.DATA[5] = vel[0] # Determines direction 00 for pos, FF for neg (HEX signed 2s complement) # Dir
        msgCanMessage.DATA[6] = 0x00 # Empty
        msgCanMessage.DATA[7] = 0x00 # Empty
        return msgCanMessage


    def get_read_can_speed_message(self):
        print('running read can speed')
        # 40h 0Bh 20h 00h 00h 00h 00h 00h
        msgCanMessage = TPCANMsg()
        msgCanMessage.ID = 0x601
        msgCanMessage.LEN = 8
        msgCanMessage.MSGTYPE = PCAN_MESSAGE_STANDARD.value
        msgCanMessage.DATA[0] = 0x40
        msgCanMessage.DATA[1] = 0x0B
        msgCanMessage.DATA[2] = 0x20
        msgCanMessage.DATA[3] = 0x00
        msgCanMessage.DATA[4] = 0x00
        msgCanMessage.DATA[5] = 0x00
        msgCanMessage.DATA[6] = 0x00
        msgCanMessage.DATA[7] = 0x00
        return msgCanMessage

    def get_read_motor_speed_message(self):
        print('running read motor speed')
        # 40h 6Ch 60h 03h 00h 00h 00h 00h
        msgCanMessage = TPCANMsg()
        msgCanMessage.ID = 0x601
        msgCanMessage.LEN = 8
        msgCanMessage.MSGTYPE = PCAN_MESSAGE_STANDARD.value
        msgCanMessage.DATA[0] = 0x40
        msgCanMessage.DATA[1] = 0x6C
        msgCanMessage.DATA[2] = 0x60
        msgCanMessage.DATA[3] = 0x03
        msgCanMessage.DATA[4] = 0x00
        msgCanMessage.DATA[5] = 0x00
        msgCanMessage.DATA[6] = 0x00
        msgCanMessage.DATA[7] = 0x00
        return msgCanMessage


    def get_velocity_mode_message(self):
        print('running velocity mode message')
        # 2Fh 60h 60h 00h 03h 00h 00h 00h
        msgCanMessage = TPCANMsg()
        msgCanMessage.ID = 0x601
        msgCanMessage.LEN = 8
        msgCanMessage.MSGTYPE = PCAN_MESSAGE_STANDARD.value
        msgCanMessage.DATA[0] = 0x2F
        msgCanMessage.DATA[1] = 0x60
        msgCanMessage.DATA[2] = 0x60
        msgCanMessage.DATA[3] = 0x00
        msgCanMessage.DATA[4] = 0x03
        msgCanMessage.DATA[5] = 0x00
        msgCanMessage.DATA[6] = 0x00
        msgCanMessage.DATA[7] = 0x00
        return msgCanMessage


    def get_position_mode_message(self):
        print('running position mode message')
        # 2Fh 60h 60h 00h 01h 00h 00h 00h
        msgCanMessage = TPCANMsg()
        msgCanMessage.ID = 0x601
        msgCanMessage.LEN = 8
        msgCanMessage.MSGTYPE = PCAN_MESSAGE_STANDARD.value
        msgCanMessage.DATA[0] = 0x2F
        msgCanMessage.DATA[1] = 0x60
        msgCanMessage.DATA[2] = 0x60
        msgCanMessage.DATA[3] = 0x00
        msgCanMessage.DATA[4] = 0x01
        msgCanMessage.DATA[5] = 0x00
        msgCanMessage.DATA[6] = 0x00
        msgCanMessage.DATA[7] = 0x00
        return msgCanMessage

    def get_velocity_sync_control_message(self):
        print('running velocity sync control')
        # 2Fh 0Fh 20h 00h 01h 00h 00h 00h
        msgCanMessage = TPCANMsg()
        msgCanMessage.ID = 0x601
        msgCanMessage.LEN = 8
        msgCanMessage.MSGTYPE = PCAN_MESSAGE_STANDARD.value
        msgCanMessage.DATA[0] = 0x2F
        msgCanMessage.DATA[1] = 0x0F
        msgCanMessage.DATA[2] = 0x20
        msgCanMessage.DATA[3] = 0x00
        msgCanMessage.DATA[4] = 0x01
        msgCanMessage.DATA[5] = 0x00
        msgCanMessage.DATA[6] = 0x00
        msgCanMessage.DATA[7] = 0x00
        return msgCanMessage

    def get_velocity_async_control_message(self):
        print('running velocity Async control')
        # 2Fh 0Fh 20h 00h 00h 00h 00h 00h
        msgCanMessage = TPCANMsg()
        msgCanMessage.ID = 0x601
        msgCanMessage.LEN = 8
        msgCanMessage.MSGTYPE = PCAN_MESSAGE_STANDARD.value
        msgCanMessage.DATA[0] = 0x2F
        msgCanMessage.DATA[1] = 0x0F
        msgCanMessage.DATA[2] = 0x20
        msgCanMessage.DATA[3] = 0x00
        msgCanMessage.DATA[4] = 0x00
        msgCanMessage.DATA[5] = 0x00
        msgCanMessage.DATA[6] = 0x00
        msgCanMessage.DATA[7] = 0x00
        return msgCanMessage

    def get_clear_error_message(self):
        print('running clear error')
        # 2Bh 40h 60h 00h 80h 00h 00h 00h
        msgCanMessage = TPCANMsg()
        msgCanMessage.ID = 0x601
        msgCanMessage.LEN = 8
        msgCanMessage.MSGTYPE = PCAN_MESSAGE_STANDARD.value
        msgCanMessage.DATA[0] = 0x2B
        msgCanMessage.DATA[1] = 0x40
        msgCanMessage.DATA[2] = 0x60
        msgCanMessage.DATA[3] = 0x00
        msgCanMessage.DATA[4] = 0x80
        msgCanMessage.DATA[5] = 0x00
        msgCanMessage.DATA[6] = 0x00
        msgCanMessage.DATA[7] = 0x00
        return msgCanMessage

    def get_set_right_motor_acceleration(self):
        print('running clear error')
        # 2Bh 40h 60h 00h 80h 00h 00h 00h
        #100 ms
        msgCanMessage = TPCANMsg()
        msgCanMessage.ID = 0x601
        msgCanMessage.LEN = 8
        msgCanMessage.MSGTYPE = PCAN_MESSAGE_STANDARD.value
        msgCanMessage.DATA[0] = 0x23
        msgCanMessage.DATA[1] = 0x83
        msgCanMessage.DATA[2] = 0x60
        msgCanMessage.DATA[3] = 0x02
        msgCanMessage.DATA[4] = 0x64
        msgCanMessage.DATA[5] = 0x00
        msgCanMessage.DATA[6] = 0x00
        msgCanMessage.DATA[7] = 0x00
        return msgCanMessage

    def get_set_left_motor_acceleration(self):
        print('running clear error')
        # 2Bh 40h 60h 00h 80h 00h 00h 00h
        # 100ms
        msgCanMessage = TPCANMsg()
        msgCanMessage.ID = 0x601
        msgCanMessage.LEN = 8
        msgCanMessage.MSGTYPE = PCAN_MESSAGE_STANDARD.value
        msgCanMessage.DATA[0] = 0x23
        msgCanMessage.DATA[1] = 0x83
        msgCanMessage.DATA[2] = 0x60
        msgCanMessage.DATA[3] = 0x01
        msgCanMessage.DATA[4] = 0x64
        msgCanMessage.DATA[5] = 0x00
        msgCanMessage.DATA[6] = 0x00
        msgCanMessage.DATA[7] = 0x00
        return msgCanMessage
    
    def get_set_right_motor_deceleration(self):
        print('running clear error')
        # 2Bh 40h 60h 00h 80h 00h 00h 00h
        #100 ms
        msgCanMessage = TPCANMsg()
        msgCanMessage.ID = 0x601
        msgCanMessage.LEN = 8
        msgCanMessage.MSGTYPE = PCAN_MESSAGE_STANDARD.value
        msgCanMessage.DATA[0] = 0x23
        msgCanMessage.DATA[1] = 0x84
        msgCanMessage.DATA[2] = 0x60
        msgCanMessage.DATA[3] = 0x02
        msgCanMessage.DATA[4] = 0x64
        msgCanMessage.DATA[5] = 0x00
        msgCanMessage.DATA[6] = 0x00
        msgCanMessage.DATA[7] = 0x00
        return msgCanMessage

    def get_set_left_motor_deceleration(self):
        print('running clear error')
        # 2Bh 40h 60h 00h 80h 00h 00h 00h
        # 100ms
        msgCanMessage = TPCANMsg()
        msgCanMessage.ID = 0x601
        msgCanMessage.LEN = 8
        msgCanMessage.MSGTYPE = PCAN_MESSAGE_STANDARD.value
        msgCanMessage.DATA[0] = 0x23
        msgCanMessage.DATA[1] = 0x84
        msgCanMessage.DATA[2] = 0x60
        msgCanMessage.DATA[3] = 0x01
        msgCanMessage.DATA[4] = 0x64
        msgCanMessage.DATA[5] = 0x00
        msgCanMessage.DATA[6] = 0x00
        msgCanMessage.DATA[7] = 0x00
        return msgCanMessage
