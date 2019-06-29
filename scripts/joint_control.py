#!/usr/bin/env python
# Example code for control of the robot
# make sure that this is running during your simulation
import rospy
from std_msgs.msg import Float64,String
from geometry_msgs.msg import Twist
import math

speed = 0.2
decay = 0.0001

def talker():
    arm_0 = rospy.Publisher('/youbot/joint0_position_controller/command', Float64, queue_size=10)
    arm_1 = rospy.Publisher('/youbot/joint1_position_controller/command', Float64, queue_size=10)
    arm_2 = rospy.Publisher('/youbot/joint2_position_controller/command', Float64, queue_size=10)
    arm_3 = rospy.Publisher('/youbot/joint3_position_controller/command', Float64, queue_size=10)
    arm_4 = rospy.Publisher('/youbot/joint4_position_controller/command', Float64, queue_size=10)
    arm_5 = rospy.Publisher('/youbot/joint5_position_controller/command', Float64, queue_size=10)
    #velocity_publisher = rospy.Publisher('/youbot/cmd_vel', Twist, queue_size=10)
    #vel_msg = Twist()
    #vel_msg.linear.x = -(vel_msg.linear.x + speed)
    #vel_msg.linear.y = 0
    #vel_msg.linear.z = 0
    #vel_msg.angular.x = 0
    #vel_msg.angular.y = 0
    #vel_msg.angular.z = 0
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        hello_str = "hello world %s" % rospy.get_time()
        position = math.pi/6
        velocity = 0.0
        rospy.loginfo(position)
        arm_0.publish(position)
        arm_1.publish(position)
        arm_2.publish(position)
        arm_3.publish(position)
        arm_4.publish(position)
        arm_5.publish(position)
        #velocity_publisher.publish(vel_msg)
        #rospy.Subscriber("/turtle1/cmd_vel", String, callback)
        rate.sleep()

def callback(data):
	if data=="w":
		vel_msg.linear.x = -0.2
	elif data=="s":
		bot_backward()
	elif data=="a":
		bot_spot_left()
	elif data=="d":
		bot_spot_right()
	elif data=="q":
		inc_speed()
	elif data=="e":
		decr_speed()


def bot_forward():
	vel_msg.linear.x = speed

def bot_backward():
	vel_msg.linear.x = -speed

def bot_spot_left():
	vel_msg.angular.z = speed

def bot_spot_right():
	vel_msg.angular.z = -speed

def inc_speed():
	speed = speed+0.2

def decr_speed():
	speed = speed-0.2



if __name__ == '__main__':
    
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
