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
