import rospy
from sensor_msgs.msg import Joy

def callback(msg):
    rospy.loginfo(rospy.get_caller_id() + "I heard%s",msg.axes)

def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber('joy',Joy,callback)
    rospy.spin()

if __name__ == '__main__':
    listener()