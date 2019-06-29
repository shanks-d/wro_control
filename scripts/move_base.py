#!/usr/bin/env python
# Example code for control of the robot
# make sure that this is running during your simulation
import rospy
from std_msgs.msg import Float64, String
from geometry_msgs.msg import Twist
import math

def callback(key):
    # print "callback_received"
    print key.data
    if key.data == '':
        vel_msg.linear.x = 0
        vel_msg.angular.z = 0
    elif key.data == 'w':
        vel_msg.linear.x = 1
        vel_msg.angular.z = 0
    elif key.data == 's':
        vel_msg.linear.x = -1
        vel_msg.angular.z = 0
    elif key.data == 'a':
        vel_msg.linear.x = 0
        vel_msg.angular.z = 3
    elif key.data == 'd':
        vel_msg.linear.x = 0
        vel_msg.angular.z = -3

if __name__ == '__main__':
    rospy.init_node('talker', anonymous=True)
    try:
        velocity_publisher = rospy.Publisher('/youbot/cmd_vel', Twist, queue_size=10)
        rospy.Subscriber('/teleop_key',String,callback)
        vel_msg = Twist()
        vel_msg.linear.x = 0
        vel_msg.linear.y = 0
        vel_msg.linear.z = 0
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        vel_msg.angular.z = 0
        rate = rospy.Rate(10) # 10hz
        while not rospy.is_shutdown():
            velocity_publisher.publish(vel_msg)
            rate.sleep()
    except rospy.ROSInterruptException:
        pass
