#!/usr/bin/env python
import rospy
from math import cos, pi, sin, sqrt
from geometry_msgs.msg import Twist
from turtlesim.srv import TeleportAbsolute

# Teleports turtlebot to given location
def teleport_absolute_client(x, y, theta):
    rospy.wait_for_service('/turtle1/teleport_absolute')    # wait until turtlebot node is running
    try:
        teleport_absolute = rospy.ServiceProxy('/turtle1/teleport_absolute',TeleportAbsolute)   # handle for calling the teleport_absolute service
        teleport_absolute(x, y, theta)  # call service which teleports turtlebot to given coordinates
    except rospy.ServiceException,e:    # exception case if call fails
        print "Service call failed: %s" %e

# Publishes linear/angular velocity commands to turtlebot
def control_turtle():
    pub = rospy.Publisher('turtle1/cmd_vel',Twist, queue_size=10)   # publish control data to turtlebot
    rate = rospy.Rate(10)    # set publisher rate

    t = 0.0                 # time variable
    T = rospy.get_param('~T',10)   # specify parameter for period or use default

    trajectory = Twist()    # message containing control data

    while not rospy.is_shutdown():

        # calculate linear velocity
        xdot = 3.0*cos(4.0*pi*t/T)*4.0*pi/T
        ydot = 3.0*cos(2.0*pi*t/T)*2.0*pi/T
        v = sqrt(xdot**2+ydot**2)

        # calculate angular velocity
        xdotdot = -3.0*sin(4*pi*t/T)*(4.0*pi/T)**2
        ydotdot = -3.0*sin(2*pi*t/T)*(2.0*pi/T)**2
        w = (ydotdot*xdot - xdotdot*ydot) / (xdot**2 + ydot**2)

        # publish control data
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
