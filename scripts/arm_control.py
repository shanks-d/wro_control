#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64
from geometry_msgs.msg import Twist
from math import *
import time
def calculate_joint_angles(arm_array):
    return [0,arm_array[1]+2.967,arm_array[2]+2.704,arm_array[3]-2.548,arm_array[4]+3.359,arm_array[5]+2.923]
    # return arm_array

def set_pose(arm_array):
    array = calculate_joint_angles(arm_array)
    arm_0.publish(array[0])
    arm_1.publish(array[1])
    arm_2.publish(array[2])
    arm_3.publish(array[3])
    arm_4.publish(array[4])
    arm_5.publish(array[5])

def home():
    arm_array = [0,0,-pi/2,0,-pi/2,0]
    set_pose(arm_array)

if __name__ == '__main__':
    rospy.init_node('talker', anonymous=True)
    arm_0 = rospy.Publisher('/youbot/joint0_position_controller/command', Float64, queue_size=10)
    arm_1 = rospy.Publisher('/youbot/joint1_position_controller/command', Float64, queue_size=10)
    arm_2 = rospy.Publisher('/youbot/joint2_position_controller/command', Float64, queue_size=10)
    arm_3 = rospy.Publisher('/youbot/joint3_position_controller/command', Float64, queue_size=10)
    arm_4 = rospy.Publisher('/youbot/joint4_position_controller/command', Float64, queue_size=10)
    arm_5 = rospy.Publisher('/youbot/joint5_position_controller/command', Float64, queue_size=10)
    # home()
    # initialize()
    # time.sleep(5)
    pose = [0,0,0,0,-pi,0]
    # pose = [0,2.967,2.704,-2.549,1.789,2.923]
    while not rospy.is_shutdown():
        set_pose(pose)
