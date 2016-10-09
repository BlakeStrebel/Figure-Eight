ROS Command Line Tools, and Publisher/Subscriber Challenge
==========================================================

## ROS Command Line Tools and Package Analysis ##
For this section, ROS command line tools were used in order to determine information about a previously unanalyzed [package](https://github.com/NU-MSR/me495_hw1.git).

1. The node `ros_cl_demo` contains one publisher and one subscriber.
  1. The names of the topics were found by using the `rosnode info` tool. These topics are `/demo_publish_topic` and `/demo_subscriber_topic`.
  2. Running `rostopic echo` causes the messages for a topic to be printed to the screen. The message can be further analyzed using `rosmsg show`.
    * `/demo_publish_topic` contains an integer `seq` which increments by one each time a new message is published, a time `stamp`, a string containing `frame_id`, a float containing `time`, and a float containing `configuration`
    * `/demo_subscriber_topic` does not print any messages when running `rostopic echo`.
  3. Message packages were found by running `rostopic info` on each node. The `/demo_publish_topic` is of type `ME495Pub` while the `/demo_subscriber_topic` is of type `std_msgs/String`.
  4. The publisher `/demo_publish_topic` publishes data at around `50 Hz`. This rate was determined by using the `rostopic hz` tool.
  5. The `/demo_publish_topic` data was was plotted using `rqt_plot /demo_publish_topic`. From the plot, the topic is publishing configuration data that oscillates in a sinusoidal waveform from -10 to 10. It also publishes time data that increases linearly as expected.
  6. A message of type `std_msg/String` is published using the `rostopic pub` tool. This results in `Manipulated String` data being printed to the terminal where `ros_cl_demo` is running.

2. The node `ros_cl_demo` also contains one service provider.
  1. The names of all services in a package can be found using the `rossrv package` tool. The only service in the `me495_hw1` package is `ME495Srv`.
  2. The service description can be found using `rossrv show`. The `me495_hw1/ME495Srv` service requests an unsigned 32 bit integer as an input and outputs an unsigned 8 bit integer.
  3.

## Working with the turtlesim package ##
The purpose of the `figure8` package is to interface with the existing [turtlesim package](http://wiki.ros.org/turtlesim) in order to make the turtle follow a reference trajectory.

### figure8_node.py ###
The node [figure8_node.py](https://github.com/ME495-EmbeddedSystems/homework-1-f2016-BlakeStrebel/blob/master/src/figure8_node.py) serves two purposes:
  1. It calls [teleport_absolute_client(x, y, theta)](https://github.com/ME495-EmbeddedSystems/homework-1-f2016-BlakeStrebel/blob/96118884d3ad3de5734760689e6f5ff473390dfb/src/figure8_node.py#L8-L14) which initializes the turtlebot by teleporting it to a location defined by `x, y, theta`. The client calls the `/turtle1/teleport_absolute` service provided by the turtlebot package.
  2. Then, it calls [control_turtle](https://github.com/ME495-EmbeddedSystems/homework-1-f2016-BlakeStrebel/blob/96118884d3ad3de5734760689e6f5ff473390dfb/src/figure8_node.py#L17-L49) which calculates the control for the turtle and publishes these values to `turtle1/cmd_vel` using `geometry_msgs/Twist.msg`.
    * The reference trajectory for the turtlebot is given by:
    ```
    Xd(t) = 3sin(4*pi*t/T)
    Yd(t) = 3sin(2*pi*t/T)
    For t = [0,T]
    ```
    * Only the magnitudes of the linear and angular velocities of the turtlebot at a given point are used to control the turtlebot's kinematics. [The equations](https://github.com/ME495-EmbeddedSystems/homework-1-f2016-BlakeStrebel/blob/96118884d3ad3de5734760689e6f5ff473390dfb/src/figure8_node.py#L28/L36) used to calculate these magnitudes were found by solving for v and w from the governing equations:
    ```
      x' = vcos(theta)
      y' = vsin(theta)
      theta' = w
    ```

### Other package notes ###
- `figure8_node.py` contains a private parameter, [T](https://github.com/ME495-EmbeddedSystems/homework-1-f2016-BlakeStrebel/blob/96118884d3ad3de5734760689e6f5ff473390dfb/src/figure8_node.py#L22), which can be used to control the period of the reference trajectory at runtime. If no value for the private parameter is specified, it defaults to `T = 10`.
- The bag file [2016-10-09-13-49-24.bag](https://github.com/ME495-EmbeddedSystems/homework-1-f2016-BlakeStrebel/blob/master/src/2016-10-09-13-49-24.bag) contains message data which can be used to playback 30 seconds of reference trajectory tracking without starting up `figure8_node.py`.
