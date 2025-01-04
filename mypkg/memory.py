#!/usr/bin/python3
# SPDX-FileCopyrightText: 2024 Yuna Isomura
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import psutil

class SystemStatusPublisher(Node):
    def __init__(self):
        super().__init__('system_status_publisher')
        self.publisher_ = self.create_publisher(String, 'system_status', 10)
        self.timer = self.create_timer(1.0, self.publish_status)
        self.get_logger().info('System Status Publisher Node has started.')

    def publish_status(self):
        cpu_usage = psutil.cpu_percent(interval=None)
        memory_usage = psutil.virtual_memory().percent
        disk_usage = psutil.disk_usage('/').percent

        status_message = f"CPU: {cpu_usage}%, Memory: {memory_usage}%, Disk: {disk_usage}%"
        msg = String()
        msg.data = status_message

        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: "{status_message}"')



def main(args=None):
    rclpy.init(args=args)
    node = SystemStatusPublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
