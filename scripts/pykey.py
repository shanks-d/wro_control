#!/usr/bin/env python
import rospy
from std_msgs.msg import String
import pygame
import sys

def initialize():
    pygame.init()
    screen = pygame.display.set_mode((400, 300))
    pygame.key.set_repeat(10,50)
    rospy.init_node('keypress_publisher', anonymous = True)

def check_keypress():
    pub = rospy.Publisher('teleop_key',String, queue_size=10)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); #sys.exit() if sys is imported
            if event.type == pygame.KEYDOWN:
                print event.key
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
                if event.key == pygame.K_w:
                    pub.publish("w")
                if event.key == pygame.K_a:
                    pub.publish("a")
                if event.key == pygame.K_s:
                    pub.publish("s")
                if event.key == pygame.K_d:
                    pub.publish("d")
            else:
                pub.publish("")

if __name__ == '__main__':
    initialize()
    check_keypress()
