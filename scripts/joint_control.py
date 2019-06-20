#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import Float64
import math
 
def talker():
    pub_0 = rospy.Publisher('/youbot/joint0_position_controller/command', Float64, queue_size=10)
    pub_1 = rospy.Publisher('/youbot/joint1_position_controller/command', Float64, queue_size=10)
    pub_2 = rospy.Publisher('/youbot/joint2_position_controller/command', Float64, queue_size=10)
    pub_3 = rospy.Publisher('/youbot/joint3_position_controller/command', Float64, queue_size=10)
    pub_4 = rospy.Publisher('/youbot/joint4_position_controller/command', Float64, queue_size=10)
    pub_5 = rospy.Publisher('/youbot/joint5_position_controller/command', Float64, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        hello_str = "hello world %s" % rospy.get_time()
        position = math.pi/6
        rospy.loginfo(position)
        pub_0.publish(position)
        pub_1.publish(position)
        pub_2.publish(position)
        pub_3.publish(position)
        pub_4.publish(position)
        pub_5.publish(position)
        rate.sleep()
 
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
