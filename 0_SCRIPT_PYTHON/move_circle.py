#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import math

class CircleMover(Node):
    def __init__(self):
        super().__init__('circle_mover')
        self.publisher = self.create_publisher(Twist, '/cmd_vel', 10)
        timer_period = 0.1
        self.timer = self.create_timer(timer_period, self.move_in_circle)
        self.radius = 0.2  # radius
        self.linear_speed = 0.1  
        self.angular_speed = self.linear_speed / self.radius  # convert from linear to angular speed

    def move_in_circle(self):
        twist = Twist()
        twist.linear.x = self.linear_speed
        twist.angular.z = self.angular_speed
        self.publisher.publish(twist)
        self.get_logger().info(f'Linear speed: {self.linear_speed} m/s, Angular speed: {self.angular_speed} rad/s')

def main(args=None):
    rclpy.init(args=args)
    circle_mover = CircleMover()
    try:
        rclpy.spin(circle_mover)
    except KeyboardInterrupt:
        pass
    finally:
        # Stop the robot when we'll close the script
        twist = Twist()
        twist.linear.x = 0.0
        twist.angular.z = 0.0
        circle_mover.publisher.publish(twist)
        circle_mover.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
