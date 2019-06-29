#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Image
import cv2
import cv_bridge
import numpy as np

class Frame:
	def __init__(self):
		self.bridge = cv_bridge.CvBridge()

		cv2.namedWindow("window", 1)
		self.image_sub = rospy.Subscriber('/camera/depth/image_raw',Image, self.img_callback)

	def img_callback(self,data):
		# data.encoding = "32FC1"
		print data.encoding
		image = self.bridge.imgmsg_to_cv2(data,desired_encoding='bgr8')
		# hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
		cv2.imshow('window',image)
		cv2.waitKey(3)

if __name__ == '__main__':
	rospy.init_node('image_subscriber', anonymous = True)
	frame = Frame()
	rospy.spin()
