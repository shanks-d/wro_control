#!/usr/bin/env python
# Example code for control of the robot
# make sure that this is running during your simulation
import rospy
from std_msgs.msg import Float64
from geometry_msgs.msg import Twist
import math

def talker():
    arm_0 = rospy.Publisher('/youbot/joint0_position_controller/command', Float64, queue_size=10)
    arm_1 = rospy.Publisher('/youbot/joint1_position_controller/command', Float64, queue_size=10)
    arm_2 = rospy.Publisher('/youbot/joint2_position_controller/command', Float64, queue_size=10)
    arm_3 = rospy.Publisher('/youbot/joint3_position_controller/command', Float64, queue_size=10)
    arm_4 = rospy.Publisher('/youbot/joint4_position_controller/command', Float64, queue_size=10)
    arm_5 = rospy.Publisher('/youbot/joint5_position_controller/command', Float64, queue_size=10)
    velocity_publisher = rospy.Publisher('/youbot/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()
    vel_msg.linear.x = 0
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        hello_str = "hello world %s" % rospy.get_time()
        angle = 65
        position = angle*math.pi/180
        velocity = math.pi/2
        rospy.loginfo(position)
        arm_0.publish(position)
        arm_1.publish(3)                       # base roll joint (0 - 5.8)
        arm_2.publish(position)                # shoulder joint (0 - 2.7)
        arm_3.publish(-0.95*position)          # elbow joint (-5.18 - 0)
        arm_4.publish(1.6*position)            # wrist pitch (0 - 3.5)
        arm_5.publish(3)                       # wrist roll (0 - 5.8)
        velocity_publisher.publish(vel_msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
