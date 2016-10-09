#!/usr/bin/env python
import rospy
import math
from math import cos, atan2, pi, sin, tan, sqrt
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
    rate = rospy.Rate(10)

    t = 0.0 # time
    T = rospy.get_param('~period',10)

    trajectory = Twist()
    trajectory.linear.y = 0
    trajectory.linear.z = 0
    trajectory.angular.z = 0
    trajectory.angular.y = 0

    while not rospy.is_shutdown():

        # calculate control
        xdot = 3.0*cos(4.0*pi*t/T)*4.0*pi/T
        ydot = 3.0*cos(2.0*pi*t/T)*2.0*pi/T
        xdotdot = -3.0*sin(4*pi*t/T)*(4.0*pi/T)**2
        ydotdot = -3.0*sin(2*pi*t/T)*(2.0*pi/T)**2
        v = sqrt(xdot**2+ydot**2)
        w = (ydotdot*xdot - xdotdot*ydot) / (xdot**2 + ydot**2)

        # publish control
        trajectory.linear.x = v
        trajectory.angular.z = w
        pub.publish(trajectory)

        # increment time
        if t == T:
            t = 0.0
        else:
            t = t + 0.1
        rate.sleep()

if __name__ == '__main__':
    rospy.init_node('figure8_node')
    try:
        teleport_absolute_client(5, 5, 0)
        control_turtle()
    except rospy.ROSInterruptException:
        pass
