#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
## Import message types here, dont forget to update package.cml and Cmakelist


def move_pub():
    pub = rospy.Publisher('turtle1/cmd_vel',Twist, queue_size=10)
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        trajectory = Twist()

        trajectory.linear.x = 1
        trajectory.linear.y = 0
        trajectory.linear.z = 0
        trajectory.angular.x = 0
        trajectory.angular.y = 0
        trajectory.angular.y = 0

        pub.publish(trajectory)
        rate.sleep()


if __name__ == '__main__':
    rospy.init_node('figure8_node')
    try:
        move_pub()
    except rospy.ROSInterruptException:
        pass
