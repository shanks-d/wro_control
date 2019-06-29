#!/usr/bin/env python
import rospy
import sys
from std_msgs.msg import Float64
from geometry_msgs.msg import Twist
from math import *
import time

def calculate_inverse(position_vector):
    w1,w2,w3,w4,w5,w6 = position_vector[0],position_vector[1],position_vector[2],0,0,1
    ca = [0,1,1,0,1]
    sa = [-1,0,0,-1,0]
    a1,a2,a3,a4,a5 = 0,155,135,0,0
    d1,d2,d3,d4,d5 = 19,0,0,0,218
    q1 = atan2(w2,w1)
    q234 = atan2(-(cos(q1)*w4+sin(q1)*w5),-w6)
    b1 = cos(q1)*w1+sin(q1)*w2-a4*cos(q234)+d5*sin(q234)
    b2 = d1-a4*sin(q234)-d5*cos(q234)-w3
    q3 = acos(abs(b1**2+b2**2-a2**2-a3**2)/(2*a2*a3))
    q2 = atan2(b2*(a2+a3*cos(q3))-a3*sin(q3)*b1, b1*(a2+a3*cos(q3))+a3*sin(q3)*b2)
    q4 = q234 - q2 - q3
    q5 = 0
    print("Inverse Solution",q1,q2,q3,q4,q5)
    return q1,q2,q3,q4,q5

def calculate_joint_angles(arm_array):                          # function to compensate for set points in gazebo
    return [0,arm_array[0]+2.967,arm_array[1]+2.704,arm_array[2]-2.548,arm_array[3]+3.359,arm_array[4]+2.923]

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
    while not rospy.is_shutdown():
        try:
            position_vector = raw_input("Enter Co-ordinates [x,y,z]: ")
            q1,q2,q3,q4,q5 = calculate_inverse(position_vector)
            set_pose([q1,q2,q3,q4,q5])
        except KeyboardInterrupt:
            sys.exit()
