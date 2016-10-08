#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from turtlesim.srv import TeleportAbsolute

## Import message types here, dont forget to update package.cml and Cmakelist

def teleport_absolute_client(x, y, theta):
    rospy.wait_for_service('/turtle1/teleport_absolute')
    try:
        teleport_absolute = rospy.ServiceProxy('/turtle1/teleport_absolute',TeleportAbsolute)
        teleport_absolute(x, y, theta)
    except rospy.ServiceException,e:
        print "Service call failed: %s" %e

def control_turtle():
    pub = rospy.Publisher('turtle1/cmd_vel',Twist, queue_size=10)
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        trajectory = Twist()

        trajectory.linear.x = 1
        trajectory.linear.y = 1
        trajectory.linear.z = 0
        trajectory.angular.x = 0
        trajectory.angular.y = 1
        trajectory.angular.y = 0

        pub.publish(trajectory)
        rate.sleep()


if __name__ == '__main__':
    rospy.init_node('figure8_node')
    try:
        teleport_absolute_client(6, 6, 0)
        control_turtle()
    except rospy.ROSInterruptException:
        pass
